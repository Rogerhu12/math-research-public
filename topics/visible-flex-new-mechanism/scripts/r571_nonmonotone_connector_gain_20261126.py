#!/usr/bin/env python3
"""New C2 connector designs from the already paid R571 phase-zero tail.

This program does not recompute the tail Riccati problem. It adopts the
identified phase-zero outer Cauchy data and its two observed variations.
All science belongs to public Actions. A profile is a new static metric,
not a finite isometric deformation or frozen-metric refinement.
"""
import argparse
from dataclasses import asdict, dataclass, replace
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import expit

SCHEMA = "r571-paid-phase-zero-tail-nonmonotone-connector-gain-v1"
RC, R0, ELL, AMP, MU = .22, .30, .2, .8, 4.0
TAIL_HESSIAN_BOUND = 75 * math.exp(-2.5) + 108 * math.exp(-3)
COUNTS = {"AD_chart_RHS": 0, "regular_core_RHS": 0,
          "quadrature_integrand": 0, "spatial_jet_points": 0, "flows": 0}
SOURCE = {
    "run_id": 45777456573, "job_id": 139764481718,
    "source_commit": "45e301661dc4101e0a9652cbf49f14133f3dc94e",
    "raw_job_log_sha256": "6f94e4dec5d8eb5a842b146967c1af601c9d0ee7ea1a2749e45de959946f8a02",
    "tag": "R571_PHASE_ZERO_SEED", "phase": 0.0, "M": 25,
    "rtol": 2.5e-12, "atol": 2.5e-14,
    "normalization": "y(alpha_17)=1, divided by exp(common_display_log_scale)",
    "common_display_log_scale": 1559.1449362672672,
    "outer_jet_names": ["F", "F_r", "F_rr", "F_rrr", "A", "A_r", "A_rr",
                        "u", "u_r", "u_rr", "v", "v_r", "v_rr"],
    "outer_jets": [-.7065905322340063, -8.845283168847214, -61.27087098510052,
                   586.8561356702817, -.0013860074803033096, -.2128688885766501,
                   -24.12103473728373, -.006930037401516542, -1.0412443182115283,
                   -113.66354489834181, 4.710603548226709, 43.26654263155906,
                   120.0288556902764],
    "coarse_to_fine_outer_delta": [-1.895925527684028e-9, -2.373374918818172e-8,
                   -1.64395821400376e-7, 1.5735522538307123e-6, -3.71879415282661e-12,
                   -5.711719430756546e-10, -6.472162183968067e-8, -1.8593970980973484e-11,
                   -2.7938791280490705e-9, -3.0498226522013283e-7, 1.2639504554101677e-8,
                   1.1609331806994305e-7, 3.220165751827153e-7],
    "fine_to_M_plus_1_outer_delta": [4.107825191113079e-15, 5.861977570020827e-14,
                   3.268496584496461e-13, 3.637978807091713e-12, 4.9873299934333204e-18,
                   1.4988010832439613e-15, 1.4921397450962104e-13, 2.42861286636753e-17,
                   6.439293542825908e-15, 7.105427357601002e-13, -2.930988785010413e-14,
                   -2.913225216616411e-13, -2.1316282072803006e-13],
    "tail_sampled_absolute_peaks_first_seven_jets": [.7065905322340063,
                   65.0085703973238, 79312.94586735596, 290076800.1096391,
                   .0013860074803033096, .2128688885766501, 24.12103473728373],
    "tail_nodes": 257,
    "tail_table_sha256": "39b0e234f2a0b6951f84ec9ea7ad263f1db078990e216e1bd9449e05f568a290",
    "source_variations_are_observations_not_certified_ODE_error_bounds": True,
}


def emit(tag, data):
    print(tag + " " + json.dumps(data, sort_keys=True, separators=(",", ":"),
                                 allow_nan=False), flush=True)


@dataclass(frozen=True)
class Profile:
    R: float = .75
    log_suppression: float = 10.0
    gain_height: float = 1.0
    core_scale: float = 1.0
    drop_end: float = .34
    gain_start: float = .37
    gain_peak: float = .48
    gain_end: float = .61
    core_start: float = .55
    alpha: float = .55
    beta: float = 1.1
    core_height: float = .04
    ball_budget: float = 1.05
    reach_budget: float = .063
    target_core_support: float = 1.0

    @property
    def m(self):
        return 1 / (1 - self.alpha)

    @property
    def radial_width(self):
        return self.R - R0

    @property
    def switch_radius(self):
        return self.core_start + .8 * (self.R - self.core_start)

    def x_of_r(self, r):
        return ((self.R - np.asarray(r)) / self.radial_width) ** (1 / self.m)


def step_and_first(value):
    value = np.asarray(value, dtype=float)
    step = np.where(value >= 1, 1.0, 0.0)
    derivative = np.zeros_like(value)
    active = (value > 0) & (value < 1)
    x = value[active]
    s = expit(-1 / x + 1 / (1 - x))
    step[active] = s
    derivative[active] = s * (1 - s) * (x ** -2 + (1 - x) ** -2)
    return step, derivative


def tail_w(r):
    r = np.asarray(r, dtype=float)
    w, wr = np.zeros_like(r), np.zeros_like(r)
    active = r > RC
    u = ELL / (r[active] - RC)
    w[active] = AMP * np.exp(-u * (2 - np.sin(u)))
    wr[active] = w[active] * (u * u * (2 - np.sin(u)) - u ** 3 * np.cos(u)) / ELL
    return w, wr


def finite_slope(par, r):
    r = np.asarray(r, dtype=float)
    w, wr = tail_w(r)
    drop, dropr = step_and_first((r - R0) / (par.drop_end - R0))
    dropr /= par.drop_end - R0
    left, leftr = step_and_first((r - par.gain_start) / (par.gain_peak - par.gain_start))
    leftr /= par.gain_peak - par.gain_start
    right, rightr = step_and_first((par.gain_end - r) / (par.gain_end - par.gain_peak))
    rightr /= -(par.gain_end - par.gain_peak)
    suppression = np.exp(-par.log_suppression * drop)
    value = w * suppression + par.gain_height * left * right
    first = (suppression * (wr - par.log_suppression * w * dropr)
             + par.gain_height * (leftr * right + left * rightr))
    return value, first


def radial_slope(par, r):
    r = np.asarray(r, dtype=float)
    value, first = finite_slope(par, r)
    value, first = np.asarray(value).copy(), np.asarray(first).copy()
    active = r > par.core_start
    t = (r[active] - par.core_start) / (par.R - par.core_start)
    b = par.core_scale * t ** par.beta / (1 - t * t) ** par.alpha
    br = b / (par.R - par.core_start) * (par.beta / t + 2 * par.alpha * t / (1 - t * t))
    value[active] += b
    first[active] += br
    return value, first


def spatial_jets(par, x):
    x = np.asarray(x, dtype=float)
    COUNTS["spatial_jet_points"] += int(x.size)
    m, d = par.m, par.radial_width
    a = par.R - d * x ** m
    ax = -d * m * x ** (m - 1)
    axx = -d * m * (m - 1) * x ** (m - 2)
    wf, wfr = finite_slope(par, a)
    gamma = d / (par.R - par.core_start)
    t = 1 - gamma * x ** m
    active = t > 0
    b, bx = np.zeros_like(x), np.zeros_like(x)
    xa, ta = x[active], t[active]
    denominator = 2 - gamma * xa ** m
    coefficient = d * m * par.core_scale * gamma ** (-par.alpha)
    b[active] = coefficient * ta ** par.beta / denominator ** par.alpha
    bx[active] = coefficient * m * gamma * xa ** (m - 1) * (
        -par.beta * ta ** (par.beta - 1) / denominator ** par.alpha
        + par.alpha * ta ** par.beta / denominator ** (par.alpha + 1))
    zx = b - ax * wf
    zxx = bx - axx * wf - ax * ax * wfr
    return a, ax, axx, zx, zxx


def initial_columns(perturbations):
    values = SOURCE["outer_jets"]
    columns = [[values[4], values[0]]]
    scales = [1.0]
    if perturbations:
        for name in ("coarse_to_fine_outer_delta", "fine_to_M_plus_1_outer_delta"):
            delta = SOURCE[name]
            column = np.array([delta[4], delta[0]])
            scale = float(np.max(np.abs(column)))
            columns.append((column / scale).tolist())
            scales.append(scale)
    return np.asarray(columns).T, np.asarray(scales)


def mean_radial_flux(r, w, A, C, Ar, Cr):
    t = (MU - 1) ** 2 / MU
    Q, Qr = t * A * A + MU * C * C, 2 * (t * A * Ar + MU * C * Cr)
    B0r = -Qr / (4 * r) + Q / (4 * r * r)
    return B0r + ((1 + 1 / MU) * Ar * Ar + Cr * Cr) / 4


def mean_x_first(a, ax, zx, A, C, Ax, Cx):
    t = (MU - 1) ** 2 / MU
    Q, Qx = t * A * A + MU * C * C, 2 * (t * A * Ax + MU * C * Cx)
    B0x = -Qx / (4 * a) + Q * ax / (4 * a * a)
    return (-((1 + 1 / MU) * Ax * Ax + Cx * Cx) / 4 - ax * B0x) / zx


def flow(par, rtol, atol, *, dense=False, perturbations=False, mean=False):
    """An AD chart means A and D=A-W*C, not automatic differentiation."""
    COUNTS["flows"] += 1
    columns, scales = initial_columns(perturbations)
    n = columns.shape[1]
    w0 = float(radial_slope(par, R0)[0])
    initial = np.r_[columns[0], columns[0] - w0 * columns[1], 0.0, 0.0]
    if mean:
        initial = np.r_[initial, 0.0]

    def rhs_ad(r, state):
        COUNTS["AD_chart_RHS"] += 1
        w, wr = (float(v) for v in radial_slope(par, r))
        A, D = state[:n], state[n:2 * n]
        Ar, Dr = (A - MU * D) / r, -(wr / w) * (A - D)
        result = np.r_[Ar, Dr, w, math.hypot(1, w)]
        if mean:
            C, Cr = (A[0] - D[0]) / w, Ar[0] / w
            J0 = mean_radial_flux(r, w, A[0], C, Ar[0], Cr)
            result = np.r_[result, J0 / w]
        return result

    first = solve_ivp(rhs_ad, (R0, par.switch_radius), initial, method="DOP853",
                      rtol=rtol, atol=atol, max_step=.004, dense_output=dense)
    if not first.success or not np.all(np.isfinite(first.y[:, -1])):
        raise ArithmeticError("A,D transfer failed: " + first.message)
    at_switch = first.y[:, -1].copy()
    ws = float(radial_slope(par, par.switch_radius)[0])
    at_switch[n:2 * n] = (at_switch[:n] - at_switch[n:2 * n]) / ws
    xs = float(par.x_of_r(par.switch_radius))

    def rhs_core(x, state):
        COUNTS["regular_core_RHS"] += 1
        a, ax, _, zx, _ = (float(v) for v in spatial_jets(par, x))
        A, C = state[:n], state[n:2 * n]
        Ax = -(MU - 1) * ax / a * A - MU * zx / a * C
        Cx = -ax / zx * Ax
        result = np.r_[Ax, Cx, -zx, -math.hypot(ax, zx)]
        if mean:
            result = np.r_[result, mean_x_first(a, ax, zx, A[0], C[0], Ax[0], Cx[0])]
        return result

    second = solve_ivp(rhs_core, (xs, 0.0), at_switch, method="DOP853",
                       rtol=rtol, atol=atol, max_step=.008, dense_output=dense)
    if not second.success or not np.all(np.isfinite(second.y[:, -1])):
        raise ArithmeticError("regular core transfer failed: " + second.message)
    final = second.y[:, -1]
    Acore, Ccore = float(final[0]), float(final[n])
    norm = math.hypot(Acore, Ccore)
    if norm == 0 or not np.all(np.isfinite(final)):
        raise ArithmeticError("nonzero actual field lost at the core")
    return {"par": par, "first": first, "second": second, "directions": n,
            "scales": scales, "final": final, "Acore": Acore, "Ccore": Ccore,
            "root_value": Ccore / norm, "rtol": rtol, "atol": atol, "mean": mean}


def sample(run, x):
    par, n = run["par"], run["directions"]
    x = np.asarray(x)
    r = par.R - par.radial_width * x ** par.m
    body = r <= par.switch_radius
    values = np.empty((len(x), len(run["final"])))
    if np.any(body):
        values[body] = run["first"].sol(r[body]).T
        w = radial_slope(par, r[body])[0]
        values[body, n:2 * n] = (values[body, :n] - values[body, n:2 * n]) / w[:, None]
    if np.any(~body):
        values[~body] = run["second"].sol(x[~body]).T
    values[:, :n] *= run["scales"][None, :]
    values[:, n:2 * n] *= run["scales"][None, :]
    return values


def field_jets(par, x, A, C):
    a, ax, axx, zx, zxx = spatial_jets(par, x)
    P, Q, H = -(MU - 1) * ax / a, -MU * zx / a, -ax / zx
    Px = -(MU - 1) * (axx / a - ax * ax / (a * a))
    Qx = -MU * (zxx / a - zx * ax / (a * a))
    Hx = -axx / zx + ax * zxx / (zx * zx)
    Ax = P * A + Q * C
    Cx = H * Ax
    Axx = Px * A + P * Ax + Qx * C + Q * Cx
    Cxx = Hx * Ax + H * Axx
    E = ax * ax + zx * zx
    half_Ex = ax * axx + zx * zxx
    As, Cs = Ax / np.sqrt(E), Cx / np.sqrt(E)
    Ass = Axx / E - Ax * half_Ex / (E * E)
    Css = Cxx / E - Cx * half_Ex / (E * E)
    return {"a": a, "ax": ax, "axx": axx, "zx": zx, "zxx": zxx, "E": E,
            "A": A, "C": C, "Ax": Ax, "Cx": Cx, "Axx": Axx, "Cxx": Cxx,
            "As": As, "Cs": Cs, "Ass": Ass, "Css": Css, "half_Ex": half_Ex}


def field_norms(g):
    a, A, C = g["a"], g["A"], g["C"]
    j = math.sqrt(MU)
    return {"V": np.hypot(A, C), "V_s": np.hypot(g["As"], g["Cs"]),
            "V_ss": np.hypot(g["Ass"], g["Css"]),
            "V_theta_over_a": np.hypot((j - 1 / j) * A, j * C) / a,
            "V_s_theta_over_a": np.hypot((j - 1 / j) * g["As"], j * g["Cs"]) / a,
            "V_theta_theta_over_a2": np.hypot((MU - 1) * A, MU * C) / (a * a)}


def mean_diagnostics(g, F0):
    a, ax, axx, zx, zxx = (g[k] for k in ("a", "ax", "axx", "zx", "zxx"))
    A, C, Ax, Cx, Axx, Cxx = (g[k] for k in ("A", "C", "Ax", "Cx", "Axx", "Cxx"))
    t = (MU - 1) ** 2 / MU
    Q = t * A * A + MU * C * C
    Qx = 2 * (t * A * Ax + MU * C * Cx)
    Qxx = 2 * (t * (Ax * Ax + A * Axx) + MU * (Cx * Cx + C * Cxx))
    B0 = -Q / (4 * a)
    B0x = -Qx / (4 * a) + Q * ax / (4 * a * a)
    B0xx = (-Qxx / (4 * a) + Qx * ax / (2 * a * a)
             + Q * axx / (4 * a * a) - Q * ax * ax / (2 * a ** 3))
    S = ((1 + 1 / MU) * Ax * Ax + Cx * Cx) / 4
    Sx = ((1 + 1 / MU) * Ax * Axx + Cx * Cxx) / 2
    F0x = (-S - ax * B0x) / zx
    F0xx = (-Sx - axx * B0x - ax * B0xx) / zx - F0x * zxx / zx
    E, half_Ex = g["E"], g["half_Ex"]
    F0s = F0x / np.sqrt(E)
    F0ss = F0xx / E - F0x * half_Ex / (E * E)
    B0s = B0x / np.sqrt(E)
    B0ss = B0xx / E - B0x * half_Ex / (E * E)
    return {"F0_relative_to_outer": F0, "F0_s": F0s, "F0_ss": F0ss,
            "B0": B0, "mean_vector_s": np.hypot(B0s, F0s),
            "mean_vector_ss": np.hypot(B0ss, F0ss)}


def tail_integrals():
    cut = .03
    low = RC + ELL * cut
    quarter = np.pi / 2
    u_breaks = np.arange(math.ceil(ELL / (R0 - RC) / quarter), math.floor(1 / cut / quarter) + 1) * quarter
    breaks = np.unique(np.r_[low, R0, RC + ELL / u_breaks])
    breaks = breaks[(breaks >= low) & (breaks <= R0)]
    totals, errors = [0.0, 0.0], [0.0, 0.0]
    for kind in range(2):
        def integrand(r):
            COUNTS["quadrature_integrand"] += 1
            w = float(tail_w(r)[0])
            return w if kind == 0 else w * w / (math.hypot(1, w) + 1)
        for left, right in zip(breaks[:-1], breaks[1:]):
            value, error = quad(integrand, left, right, epsabs=1e-15, epsrel=2e-12, limit=100)
            totals[kind] += value
            errors[kind] += error
    height_omission = AMP * ELL * cut * math.exp(-1 / cut)
    length_omission = .5 * AMP * AMP * ELL * cut * math.exp(-2 / cut)
    return {"height": totals[0], "arc_length": R0 - RC + totals[1],
            "height_omission_upper_bound": height_omission,
            "arc_omission_upper_bound": length_omission,
            "quadrature_error_estimates_not_certificates": errors}


def tail_linear_peak_bounds(Acore):
    F, Fr, Frr, _, A, Ar, Arr = SOURCE["tail_sampled_absolute_peaks_first_seven_jets"]
    wmax = AMP * math.exp(-2.5)
    correction = wmax * TAIL_HESSIAN_BOUND
    values = {"V": math.hypot(A, F), "V_s": math.hypot(Ar, Fr),
              "V_ss": math.hypot(Arr + correction * Ar, Frr + correction * Fr),
              "V_theta_over_a": math.hypot(1.5 * A, 2 * F) / RC,
              "V_s_theta_over_a": math.hypot(1.5 * Ar, 2 * Fr) / RC,
              "V_theta_theta_over_a2": math.hypot(3 * A, 4 * F) / RC ** 2}
    return {name: value / abs(Acore) for name, value in values.items()}


def extrema(fields, x, r):
    rows = []
    for name, value in fields.items():
        i = int(np.argmax(np.abs(value)))
        rows.append({"field": name, "absolute_max": float(abs(value[i])),
                     "signed_value": float(value[i]), "x": float(x[i]), "r": float(r[i])})
    return rows


def gain_transversality(run):
    """Compact-support Green identity; no additional ODE or finite difference.

    The normalized core A is identically one. Since the H variation vanishes
    near both physical endpoints, the boundary identity remains valid even
    when the numerically selected core C is small and not exactly zero.
    """
    par, n, Acore = run["par"], run["directions"], run["Acore"]

    def integrand(r):
        COUNTS["quadrature_integrand"] += 1
        left = float(step_and_first((r - par.gain_start) / (par.gain_peak - par.gain_start))[0])
        right = float(step_and_first((par.gain_end - r) / (par.gain_end - par.gain_peak))[0])
        w = float(radial_slope(par, r)[0])
        state = run["first"].sol(r)
        A, D = float(state[0]) / Acore, float(state[n]) / Acore
        C = (A - D) / w
        return left * right * (MU * (MU - 1) * C * C - (MU - 1) ** 2 * (A / w) ** 2) / (r * r)

    breaks = sorted({par.gain_start, par.gain_peak, par.core_start, par.gain_end})
    breaks = [r for r in breaks if par.gain_start <= r <= par.gain_end]
    total, error = 0.0, 0.0
    for left, right in zip(breaks[:-1], breaks[1:]):
        value, estimate = quad(integrand, left, right, epsabs=1e-10, epsrel=2e-10, limit=150)
        total += value
        error += estimate
    return {"D_integral": total, "d_core_C_over_A_d_gain_height": -par.R / (MU - 1) * total,
            "QUADPACK_absolute_error_estimate_not_certificate": error,
            "ODE_error_is_not_included_in_the_quadrature_error_estimate": True,
            "identity_uses_same_signed_A_core_normalization": True}


def report(run, tail, nodes):
    par, n = run["par"], run["directions"]
    feature_r = [par.drop_end, par.gain_start, par.gain_peak, par.gain_end,
                 par.core_start, par.switch_radius]
    endpoint_points = 10.0 ** -np.arange(1, 13)
    x = np.unique(np.r_[np.linspace(0, 1, nodes), endpoint_points, 1 - endpoint_points,
                        par.x_of_r(np.asarray(feature_r))])
    values = sample(run, x)
    Acore = run["Acore"]
    if Acore == 0:
        raise ArithmeticError("unit-core report requires nonzero Acore")
    g = field_jets(par, x, values[:, 0] / Acore, values[:, n] / Acore)
    a, ax, axx, zx, zxx, E = (g[k] for k in ("a", "ax", "axx", "zx", "zxx", "E"))
    total_height, total_length = float(run["final"][2 * n]), float(run["final"][2 * n + 1])
    z = par.core_height + total_height - values[:, 2 * n]
    cap_height = par.core_height + total_height + tail["height"]
    arc = total_length + tail["arc_length"]
    meridional = (ax * zxx - zx * axx) / E ** 1.5
    parallel = zx / (a * np.sqrt(E))
    body_curvature = np.maximum(np.abs(meridional), np.abs(parallel))
    max_curvature = max(float(np.max(body_curvature)), TAIL_HESSIAN_BOUND, 1 / par.R)
    body_ball = np.sqrt(a * a + z * z)
    # The tail bound is conservative over the whole radial tail, not a new
    # sampled tail field. Heights themselves retain their quadrature status.
    ball = max(float(np.max(body_ball)), math.hypot(R0, cap_height),
               math.hypot(par.R, par.core_height))
    mirror = min(float(np.min(z * z - par.reach_budget ** 2 * ax * ax / E)),
                 (par.core_height + total_height) ** 2 - par.reach_budget ** 2)
    target_chord = math.hypot(par.target_core_support - RC, cap_height - par.core_height)
    current_chord = math.hypot(par.R - RC, cap_height - par.core_height)
    slacks = {"ball": 1 - ball * ball / par.ball_budget ** 2,
              "curvature": 1 - par.reach_budget * max_curvature,
              "mirror_necessary": mirror / par.reach_budget ** 2,
              "target_core_to_fixed_cap_chord": arc / target_chord - 1,
              "core_perimeter_support_necessary": np.pi * par.R / (2 * par.target_core_support) - 1}
    linear = field_norms(g)
    tail_bounds = tail_linear_peak_bounds(Acore)
    linear_cost = max(max(float(np.max(v)) for v in linear.values()), max(tail_bounds.values()))
    F0 = values[:, 2 * n + 2] / (Acore * Acore)
    mean = mean_diagnostics(g, F0)
    mean_cost = max(float(np.max(np.abs(mean[k]))) for k in ("F0_s", "F0_ss", "mean_vector_s", "mean_vector_ss"))
    perturbation_reports = []
    if n > 1:
        for col, name, sign in ((1, "source_coarse_to_fine", -1), (2, "source_fine_to_M_plus_1", 1)):
            Ac = Acore + sign * float(run["final"][col]) * run["scales"][col]
            Cc = run["Ccore"] + sign * float(run["final"][n + col]) * run["scales"][col]
            other = field_jets(par, x, (values[:, 0] + sign * values[:, col]) / Ac,
                               (values[:, n] + sign * values[:, n + col]) / Ac)
            difference = max(float(np.max(np.abs(other[k] - g[k])))
                             for k in ("A", "C", "As", "Cs", "Ass", "Css"))
            perturbation_reports.append({"source": name,
                "variant_minus_base_core_ratio": Cc / Ac - run["Ccore"] / Acore,
                "maximum_unit_core_two_jet_component_difference": difference,
                "observation_not_certified_error_bound": True})
    return {"profile": asdict(par), "A_core_in_paid_display_scale": Acore,
            "C_core_over_A": run["Ccore"] / Acore,
            "core_A_over_paid_outer_A": Acore / SOURCE["outer_jets"][4],
            "connector_nodes_including_features": len(x), "geometry_slacks": slacks,
            "all_declared_necessary_geometry_rows_nonnegative_on_this_scan": min(slacks.values()) >= -1e-8,
            "geometry": {"cap_height": cap_height, "total_meridian_arc_to_flat_disk_boundary": arc,
                "core_to_cap_height_difference": cap_height - par.core_height,
                "current_circle_to_fixed_cap_nearest_chord": current_chord,
                "target_support_to_fixed_cap_nearest_chord": target_chord,
                "ball_bound_with_sampled_body_and_full_tail_envelope": ball,
                "curvature_max_with_sampled_body_and_proved_tail_bound": max_curvature,
                "body_curvature_attainers": extrema({"meridional": meridional, "parallel": parallel}, x, a),
                "coordinate_E_min": float(np.min(E)),
                "fixed_cap_diameter_over_declared_diameter_bound": RC / par.ball_budget,
                "macro_core_strip_and_finite_amplitude_are_not_paid": True},
            "unit_core_linear_peaks": extrema(linear, x, a),
            "old_tail_node_peak_upper_bounds_after_same_core_normalization": tail_bounds,
            "old_tail_unsampled_points_are_not_covered_by_these_field_bounds": True,
            "unit_core_quadratic_mean_peaks": extrema(mean, x, a),
            "mean_height_increment_core_minus_outer": float(run["final"][2 * n + 2] / (Acore * Acore)),
            "mean_height_gauge_is_outer_value_zero": True,
            "full_tail_mean_height_integral_not_recomputed": True,
            "linear_C2_cost_observation": linear_cost,
            "quadratic_mean_derivative_cost_observation": mean_cost,
            "compact_gain_control_transversality": gain_transversality(run),
            "source_variation_propagation": perturbation_reports,
            "finite_grid_only": True, "full_pair_reach_certified": False,
            "j4_forced_response_or_complete_nonlinear_solution_paid": False}


class DeclaredClockReached(RuntimeError):
    pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--maximum-seconds", type=float, default=2400)
    parser.add_argument("--scan-heights", type=int, default=33)
    parser.add_argument("--report-nodes", type=int, default=1025)
    parser.add_argument("--final-nodes", type=int, default=4097)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--amplitude-ranking-probe", type=float, default=.001)
    args = parser.parse_args()
    started = time.monotonic()
    deadline = started + args.maximum_seconds
    if args.scan_heights < 3 or args.report_nodes < 5 or args.final_nodes < args.report_nodes:
        raise ValueError("invalid declared scan")
    radii, suppressions, core_scales = (.75, .85), (6.0, 10.0, 14.0), (.5, 1.0, 1.5, 2.0)
    heights = np.geomspace(.02, 4.0, args.scan_heights)
    definition = {"schema": SCHEMA, "source": SOURCE, "arguments": vars(args),
        "this_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "R_values": radii, "log_suppression_values": suppressions, "core_scale_values": core_scales,
        "gain_height_scan": {"minimum": .02, "maximum": 4.0, "count": args.scan_heights, "spacing": "log"},
        "background_formula": "W=w_phi0*exp(-L*step_drop)+H*step_up*step_down+delayed_core_term",
        "core_term": "lambda*t^beta/(1-t^2)^alpha, t=(r-core_start)/(R-core_start), zero below core_start",
        "parameter_chart": "A,D=A-W*C until core_start+.8*(R-core_start); then regular x with r=R-(R-.30)x^m",
        "mean_flux": "R575 J0=B0_r+((1+1/j^2)A_r^2+C_r^2)/4; true incoming flux is not set to zero",
        "root_equation": "C_core/hypot(A_core,C_core)=0, scalar gain-height control",
        "design_metric_changes_with_profile": True, "old_tail_Riccati_replayed": False,
        "source_small_Cauchy_state_is_reused_with_its_observed_variations": True,
        "ranking_probe_is_not_a_proved_nonlinear_radius": True,
        "finite_amplitude_or_README_completion_claim": False}
    emit("GAIN_DEFINITION", definition)
    tail = tail_integrals()
    emit("GAIN_FIXED_TAIL_GEOMETRY", tail)
    candidates, censuses = [], []
    termination = "declared_parameter_census_completed"

    def check_clock():
        if time.monotonic() >= deadline:
            raise DeclaredClockReached("declared scientific segment reached before next actual flow")

    try:
        for R in radii:
            for L in suppressions:
                for scale in core_scales:
                    base = Profile(R=R, log_suppression=L, core_scale=scale)
                    cache = {}

                    def objective(H):
                        key = float(H)
                        if key not in cache:
                            check_clock()
                            result = flow(replace(base, gain_height=key), args.rtol, args.atol)
                            cache[key] = result["root_value"]
                        return cache[key]

                    roots = []
                    previous_H, previous_value = None, None
                    for H in heights:
                        value = objective(float(H))
                        if value == 0:
                            roots.append(float(H))
                        elif previous_value is not None and value * previous_value < 0:
                            root = brentq(objective, previous_H, float(H), xtol=2e-12,
                                          rtol=4 * np.finfo(float).eps)
                            if all(abs(root - old) > 1e-9 for old in roots):
                                roots.append(float(root))
                        previous_H, previous_value = float(H), value
                    census = {"R": R, "log_suppression": L, "core_scale": scale,
                              "actual_distinct_flow_calls": len(cache), "root_heights": roots,
                              "no_sign_change_is_not_a_no_root_theorem": True}
                    censuses.append(census)
                    emit("GAIN_BRACKET_CENSUS", census)
                    for H in roots:
                        check_clock()
                        actual = flow(replace(base, gain_height=H), args.rtol, args.atol,
                                      dense=True, mean=True)
                        result = report(actual, tail, args.report_nodes)
                        eps = args.amplitude_ranking_probe
                        result["ranking_partial_curvature_proxy"] = (eps * result["linear_C2_cost_observation"]
                            + eps * eps * result["quadratic_mean_derivative_cost_observation"])
                        result["proxy_omits_mode4_and_nonlinear_remainder"] = True
                        candidates.append(result)
                        emit("GAIN_CANDIDATE", result)
    except DeclaredClockReached:
        termination = "declared_scientific_clock_checkpoint"
    feasible = [x for x in candidates
                if x["all_declared_necessary_geometry_rows_nonnegative_on_this_scan"]
                and abs(x["C_core_over_A"]) <= 1e-7]
    selected = min(feasible, key=lambda x: x["ranking_partial_curvature_proxy"]) if feasible else None
    refined = None
    if selected is not None and time.monotonic() < deadline:
        par = Profile(**selected["profile"])
        final_run = flow(par, args.rtol / 8, args.atol / 8,
                         dense=True, perturbations=True, mean=True)
        refined = report(final_run, tail, args.final_nodes)
        refined["same_profile_tolerance_and_radial_node_refinement"] = True
        refined["core_ratio_change_from_selection"] = refined["C_core_over_A"] - selected["C_core_over_A"]
    ranked = sorted(candidates, key=lambda x: (
        not x["all_declared_necessary_geometry_rows_nonnegative_on_this_scan"],
        x["ranking_partial_curvature_proxy"]))[:8]
    final = {"definition": definition, "termination": termination,
             "completed_parameter_censuses": len(censuses), "candidate_roots": len(candidates),
             "finite_necessary_geometry_and_core_residual_accepted": len(feasible),
             "best_candidate_summaries": ranked, "selected_refined": refined,
             "actual_work_counts": COUNTS, "elapsed_seconds": time.monotonic() - started,
             "fixed_metric_refinement_demonstrated": False, "finite_nonlinear_branch_constructed": False,
             "README_completion_claim": False}
    emit("GAIN_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("GAIN_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
