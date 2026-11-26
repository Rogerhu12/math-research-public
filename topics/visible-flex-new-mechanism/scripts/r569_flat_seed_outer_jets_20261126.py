#!/usr/bin/env python3
"""Numerical realization of the fixed R569 linear seed and its outer jets.

This program is for public Actions execution. It does not emit a finite
isometric family or a cutoff embedding. The exact mathematical seed is
R569's infinite DtN/Riccati limit. Finite integrations use precisely
rho_{M+1}=0, normalize y(alpha_160)=1, and keep logarithmic scales while
extending outward. M/M+1 and tolerance comparisons remain observations,
separate from R569's exact-DtN truncation bound.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

SCHEMA = "r569-flat-linear-seed-numerical-interface-v1"
RC, ELL, AMP = 0.22, 0.2, 0.1
FIRST_PEAK = 160
OUTER_RADIUS = 0.30
JET_NAMES = ["f", "f_r", "f_rr", "f_rrr", "a", "a_r", "a_rr",
             "u_amplitude", "u_amplitude_r", "u_amplitude_rr",
             "v_amplitude", "v_amplitude_r", "v_amplitude_rr"]


def emit(tag, data):
    print(tag + " " + json.dumps(data, sort_keys=True, separators=(",", ":"),
                                allow_nan=False), flush=True)


def coefficients(u):
    r = RC + ELL / np.sqrt(u)
    ru = -ELL / (2 * u ** 1.5)
    eps = 0.12 / (r * r * u ** 3)
    eps_log_derivative = -3 / u - 2 * ru / r
    g = (np.sqrt(u) * np.cos(u) - (2 - np.sin(u)) / (2 * np.sqrt(u))
         + 1.5 / u - 0.8 / (r * u ** 1.5))
    gp = (np.cos(u) / np.sqrt(u) - np.sqrt(u) * np.sin(u)
          + (2 - np.sin(u)) / (4 * u ** 1.5) - 1.5 / u ** 2
          + 0.8 * ru / (r * r * u ** 1.5) + 1.2 / (r * u ** 2.5))
    return r, eps, g, eps_log_derivative, gp


def maximum_point(n):
    center = np.pi / 2 + 2 * np.pi * n
    if n < FIRST_PEAK:
        raise ValueError("proved stationary-point bracket starts at peak 160")
    return brentq(lambda u: coefficients(u)[2], center - .003, center,
                  xtol=5e-13, rtol=4 * np.finfo(float).eps)


def rhs(u, state):
    # z=y_u/epsilon balances the derivative at high-contrast maxima.
    _, eps, g, elog, _ = coefficients(u)
    y, z = state
    return [eps * z, -y - (g + elog) * z]


def integrate(left, right, state, rtol, atol, max_step, dense=False):
    result = solve_ivp(rhs, (left, right), state, method="DOP853",
                       rtol=rtol, atol=atol, max_step=max_step,
                       dense_output=dense)
    if not result.success or not np.all(np.isfinite(result.y[:, -1])):
        raise ArithmeticError("linear transfer failed: " + str(result.message))
    return result


def inner_slope(M, rtol, atol, max_step):
    """Finite tail rho_{M+1}=0 means y(alpha_{M+1})=0, not y(alpha_M)=0."""
    if M < FIRST_PEAK + 1:
        raise ValueError("M must be at least 161")
    state = np.array([0.0, 1.0])
    high = maximum_point(M + 1)
    nfev, peak_records = 0, []
    rho161 = None
    for n in range(M, FIRST_PEAK - 1, -1):
        low = maximum_point(n)
        incoming_y = float(state[0])
        sol = integrate(high, low, state, rtol, atol, max_step)
        nfev += sol.nfev
        outgoing = sol.y[:, -1]
        scale = float(outgoing[0])
        if not np.isfinite(scale) or scale == 0:
            raise ArithmeticError("peak normalization lost its nonzero y component")
        rho = -incoming_y / scale
        if n < M and not (0 < rho < 1 / 32):
            raise ArithmeticError("numerical transfer contradicted the proved positive small ratio")
        if n == FIRST_PEAK:
            rho161 = rho
        peak_records.append({"cell": n, "rho_at_inner_peak": rho,
                             "balanced_slope_at_outer_peak": float(outgoing[1] / scale),
                             "nfev": int(sol.nfev)})
        state = outgoing / scale
        high = low
    alpha = maximum_point(FIRST_PEAK)
    # Bound for exact DtN input only; it does not include numerical solve_ivp error.
    log_rho_bound = -np.log(32.0) - 3 * (M - FIRST_PEAK) * np.log(10.0)
    log_balanced_slope_bound = (np.log(8.0) + 3 * np.log(alpha)
                                - 1.5 * np.sqrt(alpha) + log_rho_bound)
    return {
        "M": M, "terminal_peak_index": M + 1,
        "terminal_condition": "rho_{M+1}=0; y(alpha_{M+1})=0",
        "alpha160": alpha, "y_at_alpha160": 1.0,
        "z_at_alpha160": float(state[1]), "rho161": float(rho161),
        "nfev_inner": int(nfev), "transfer_records": peak_records,
        "exact_DtN_rho161_truncation_log_upper_bound": float(log_rho_bound),
        "exact_DtN_z_at_alpha160_truncation_log_upper_bound": float(log_balanced_slope_bound),
        "those_bounds_exclude_numerical_ODE_error": True,
    }


def scaled_jets(u, state):
    """All returned quantities share the caller's logarithmic amplitude."""
    r, eps, g, elog, gp = coefficients(u)
    y, z = state
    yu = eps * z
    yuu = -g * yu - eps * y
    yuuu = -gp * yu - g * yuu - eps * elog * y - eps * yu
    ur = -2 * u ** 1.5 / ELL
    urr = 6 * u ** 2 / ELL ** 2
    urrr = -24 * u ** 2.5 / ELL ** 3
    yr = yu * ur
    yrr = yuu * ur ** 2 + yu * urr
    yrrr = yuuu * ur ** 3 + 3 * yuu * ur * urr + yu * urrr
    f = r ** 4 * y
    fr = 4 * r ** 3 * y + r ** 4 * yr
    frr = 12 * r ** 2 * y + 8 * r ** 3 * yr + r ** 4 * yrr
    frrr = 24 * r * y + 36 * r ** 2 * yr + 12 * r ** 3 * yrr + r ** 4 * yrrr
    delta = u ** -.5
    w = AMP * np.exp(-(2 - np.sin(u)) / delta)
    wr = w * ((2 - np.sin(u)) / delta ** 2 - 2 * np.cos(u) / delta ** 4) / ELL
    a = w * (4 * f - r * fr) / 3
    ar = w * fr
    arr = wr * fr + w * frr
    U = 1.5 * a / r
    Ur = 1.5 * (ar / r - a / r ** 2)
    Urr = 1.5 * (arr / r - 2 * ar / r ** 2 + 2 * a / r ** 3)
    V = -2 * f / r
    Vr = -2 * (fr / r - f / r ** 2)
    Vrr = -2 * (frr / r - 2 * fr / r ** 2 + 2 * f / r ** 3)
    return np.asarray([f, fr, frr, frrr, a, ar, arr, U, Ur, Urr, V, Vr, Vrr])


def outward_profile(inner, rtol, atol, max_step, radial_nodes):
    alpha = inner["alpha160"]
    inner_radius = RC + ELL / np.sqrt(alpha)
    radii = np.linspace(inner_radius, OUTER_RADIUS, radial_nodes)
    query_u = (ELL / (radii - RC)) ** 2
    query_u[0] = alpha
    last_u = float(query_u[-1])
    phase_breaks = np.pi / 2 + 2 * np.pi * np.arange(FIRST_PEAK + 1)
    breaks = np.r_[alpha, np.sort(phase_breaks[(phase_breaks < alpha)
                                              & (phase_breaks > last_u)])[::-1], last_u]
    state = np.array([1.0, inner["z_at_alpha160"]])
    log_scale, nfev = 0.0, 0
    jets = np.empty((radial_nodes, len(JET_NAMES)))
    logs = np.empty(radial_nodes)
    assigned = np.zeros(radial_nodes, dtype=bool)
    segments = []
    for left, right in zip(breaks[:-1], breaks[1:]):
        sol = integrate(float(left), float(right), state, rtol, atol, max_step, dense=True)
        nfev += sol.nfev
        selected = (~assigned) & (query_u <= left) & (query_u >= right)
        indices = np.flatnonzero(selected)
        for index in indices:
            jets[index] = scaled_jets(float(query_u[index]), sol.sol(float(query_u[index])))
            logs[index] = log_scale
            assigned[index] = True
        outgoing = sol.y[:, -1]
        norm = float(np.max(np.abs(outgoing)))
        if not norm > 0 or not np.isfinite(norm):
            raise ArithmeticError("outward logarithmic normalization failed")
        log_scale += np.log(norm)
        state = outgoing / norm
        segments.append({"u_from": float(left), "u_to": float(right),
                         "log_scale_at_exit": float(log_scale), "nfev": int(sol.nfev)})
    if not np.all(assigned) or not np.all(np.isfinite(jets)) or not np.all(np.isfinite(logs)):
        raise ArithmeticError("incomplete finite outer seed table")
    outer_norm = math.hypot(float(jets[-1, 0]), (OUTER_RADIUS - RC) * float(jets[-1, 1]))
    if not outer_norm > 0:
        raise ArithmeticError("nonzero outer Cauchy normalization was lost")
    return {"radii": radii, "u": query_u, "jets": jets, "log_scales": logs,
            "outer_cauchy_log_norm": float(logs[-1] + np.log(outer_norm)),
            "nfev_outer": int(nfev), "segments": segments}


def display_profile(profile, common_log_scale):
    jets = profile["jets"]
    delta = profile["log_scales"][:, None] - common_log_scale
    zero = jets == 0
    logabs = np.zeros_like(jets)
    logabs[~zero] = np.log(np.abs(jets[~zero]))
    exponents = logabs + delta
    if np.any(exponents[~zero] > np.log(np.finfo(float).max)):
        raise OverflowError("common display scale does not fit all seed derivatives")
    with np.errstate(under="ignore"):
        values = np.where(zero, 0.0, np.sign(jets) * np.exp(exponents))
    return values


def calculate(M, rtol, atol, max_step, radial_nodes):
    inner = inner_slope(M, rtol, atol, max_step)
    profile = outward_profile(inner, rtol, atol, max_step, radial_nodes)
    return {"inner": inner, "profile": profile, "rtol": rtol, "atol": atol}


def comparison(left, right, common_log_scale):
    lv = display_profile(left["profile"], common_log_scale)
    rv = display_profile(right["profile"], common_log_scale)
    difference = rv - lv
    denominator = max(float(np.linalg.norm(lv[-1])), 1e-300)
    c2_columns = [7, 8, 9, 10, 11, 12]
    return {
        "same_y_alpha160_normalization_before_any_display_scaling": True,
        "z_alpha160_difference": right["inner"]["z_at_alpha160"] - left["inner"]["z_at_alpha160"],
        "rho161_difference": right["inner"]["rho161"] - left["inner"]["rho161"],
        "outer_jet_difference_in_common_display_scale": difference[-1].tolist(),
        "outer_jet_relative_l2_difference": float(np.linalg.norm(difference[-1]) / denominator),
        "sampled_unit_T_C2_difference_max": float(np.max(np.abs(difference[:, c2_columns]))),
        "sampled_table_difference_max": float(np.max(np.abs(difference))),
        "comparison_is_not_a_certified_numerical_ODE_error_bound": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--M", type=int, default=168)
    parser.add_argument("--radial-nodes", type=int, default=129)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.15)
    parser.add_argument("--tolerance-refinement", type=float, default=8.0)
    args = parser.parse_args()
    if args.radial_nodes < 3 or args.tolerance_refinement <= 1:
        raise ValueError("at least three output radii and an actual tolerance refinement are required")
    started = time.monotonic()
    definition = {
        "schema": SCHEMA, "arguments": vars(args),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixed_profile": {"rc": RC, "ell": ELL, "A": AMP,
                          "w": "A*exp(-(2-sin(delta^-2))/delta)"},
        "equation": "(w*f_r)_r-4*w_r*f/r=0",
        "transformed": "(p*y_u)_u+epsilon*p*y=0; f=r^4*y",
        "state": "y,z=y_u/epsilon; normalized y(alpha160)=1 before outer extension",
        "terminal_indexing": "input M imposes rho_{M+1}=0 at alpha_{M+1}",
        "unit_T_seed": "delta_u=3*a/(2*r)*sin(2theta), delta_v=-2*f/r*sin(2theta)",
        "a_definition": "a=w*(4*f-r*f_r)/3",
        "radius_and_mean_height_first_variations": "zero",
        "fixed_metric": "(1+w^2)*dr^2+r^2*dtheta^2",
        "open_hat": "exact mathematical f,a,V all vanish to all orders at rc and are zero for r<=rc",
        "table_does_not_replace_the_infinite_inner_seed_by_a_finite_cutoff": True,
        "nonlinear_equal_metric_family_constructed": False,
        "README_completion_claim": False,
    }
    emit("R569_SEED_DEFINITION", definition)
    coarse = calculate(args.M, args.rtol, args.atol, args.max_step, args.radial_nodes)
    emit("R569_SEED_TRANSFER", {"run": "M_coarse", **coarse["inner"],
                               "nfev_outer": coarse["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": coarse["profile"]["outer_cauchy_log_norm"]})
    fine_rtol = args.rtol / args.tolerance_refinement
    fine_atol = args.atol / args.tolerance_refinement
    fine = calculate(args.M, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    emit("R569_SEED_TRANSFER", {"run": "M_finer_tolerance", **fine["inner"],
                               "nfev_outer": fine["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": fine["profile"]["outer_cauchy_log_norm"]})
    nextM = calculate(args.M + 1, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    emit("R569_SEED_TRANSFER", {"run": "M_plus_1_finer_tolerance", **nextM["inner"],
                               "nfev_outer": nextM["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": nextM["profile"]["outer_cauchy_log_norm"]})
    common_log_scale = fine["profile"]["outer_cauchy_log_norm"]
    values = display_profile(fine["profile"], common_log_scale)
    result = {
        "definition": definition,
        "common_display_log_scale_relative_to_y_alpha160_equals_1": common_log_scale,
        "display_values_mean_exact_alpha160_scale_times_exp_minus_common_log_scale": True,
        "numerical_ODE_transfer_observation": comparison(coarse, fine, common_log_scale),
        "finite_tail_M_vs_M_plus_1_observation": comparison(fine, nextM, common_log_scale),
        "seed_table": {"jet_names": JET_NAMES,
                       "radii": fine["profile"]["radii"].tolist(),
                       "u": fine["profile"]["u"].tolist(),
                       "jets_in_common_display_scale": values.tolist()},
        "outer_port": {"r": OUTER_RADIUS, "jet_names": JET_NAMES,
                       "jets_in_common_display_scale": values[-1].tolist(),
                       "s_orientation_rule": "if r=rc+L-s, first s derivatives are minus r derivatives; second are equal"},
        "inner_unsampled_interval": [RC, float(fine["profile"]["radii"][0])],
        "inner_seed_remains_the_exact_R569_limit_not_a_new_zero_annulus": True,
        "linear_seed_only": True, "all_frequency_nonlinear_inverse_not_proved": True,
        "complete": False, "elapsed_seconds": time.monotonic() - started,
    }
    emit("R569_SEED_FINAL", result)
    raw = json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("R569_SEED_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()

