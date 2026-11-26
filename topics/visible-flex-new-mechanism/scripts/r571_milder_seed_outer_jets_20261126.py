#!/usr/bin/env python3
"""Numerical realization of the fixed R571 linear seed and its outer jets.

This program is for public Actions execution. It does not emit a finite
isometric family or a cutoff embedding. The exact mathematical seed is
R571's infinite DtN/Riccati limit. Finite integrations use precisely
rho_{M+1}=0, normalize y(alpha_17)=1, and keep logarithmic scales while
extending outward. M/M+1 and tolerance comparisons remain observations,
separate from R571's exact-DtN truncation bound.
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

SCHEMA = "r571-milder-flat-linear-seed-numerical-interface-v1"
RC, ELL, AMP = 0.22, 0.2, 0.8
PHASE = 0.0
ANGULAR_MODE = 2
FIRST_PEAK = 17
OUTER_RADIUS = 0.30
JET_NAMES = ["f", "f_r", "f_rr", "f_rrr", "a", "a_r", "a_rr",
             "u_amplitude", "u_amplitude_r", "u_amplitude_rr",
             "v_amplitude", "v_amplitude_r", "v_amplitude_rr"]


def emit(tag, data):
    print(tag + " " + json.dumps(data, sort_keys=True, separators=(",", ":"),
                                allow_nan=False), flush=True)


def coefficients(u):
    r = RC + ELL / u
    ru = -ELL / u ** 2
    mu = ANGULAR_MODE ** 2
    eps = mu * (mu - 1) * ELL ** 2 / (r * r * u ** 4)
    eps_log_derivative = -4 / u - 2 * ru / r
    angle = u + PHASE
    g = (u * np.cos(angle) - (2 - np.sin(angle))
         + 2 / u - 2 * mu * ELL / (r * u ** 2))
    gp = (2 * np.cos(angle) - u * np.sin(angle) - 2 / u ** 2
          + 2 * mu * ELL * ru / (r * r * u ** 2) + 4 * mu * ELL / (r * u ** 3))
    return r, eps, g, eps_log_derivative, gp

def maximum_point(n):
    center = np.pi / 2 + 2 * np.pi * n - PHASE
    if n < FIRST_PEAK:
        raise ValueError("proved stationary-point bracket starts at peak 17")
    return brentq(lambda u: coefficients(u)[2], center - .04, center,
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
        raise ValueError("M must be at least 18")
    state = np.array([0.0, 1.0])
    high = maximum_point(M + 1)
    nfev, peak_records = 0, []
    rho_first_plus_one = None
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
            raise ArithmeticError("numerical transfer outside the declared positive-small-ratio numerical branch")
        if n == FIRST_PEAK:
            rho_first_plus_one = rho
        peak_records.append({"cell": n, "rho_at_inner_peak": rho,
                             "balanced_slope_at_outer_peak": float(outgoing[1] / scale),
                             "nfev": int(sol.nfev)})
        state = outgoing / scale
        high = low
    alpha = maximum_point(FIRST_PEAK)
    # Bound for exact DtN input only; it does not include numerical solve_ivp error.
    log_rho_bound = -np.log(32.0) - 3 * (M - FIRST_PEAK) * np.log(10.0)
    log_balanced_slope_bound = (np.log(8.0) + 21 + 4 * np.log(alpha)
                                - 1.5 * alpha + log_rho_bound)
    return {
        "M": M, "angular_mode": ANGULAR_MODE, "terminal_peak_index": M + 1,
        "terminal_condition": "rho_{M+1}=0; y(alpha_{M+1})=0",
        "alpha_first": alpha, "y_at_alpha_first": 1.0,
        "z_at_alpha_first": float(state[1]), "rho_first_plus_one": float(rho_first_plus_one),
        "nfev_inner": int(nfev), "transfer_records": peak_records,
        "exact_DtN_rho_first_plus_one_truncation_log_upper_bound": float(log_rho_bound) if ANGULAR_MODE == 2 else None,
        "exact_DtN_z_at_alpha_first_truncation_log_upper_bound": float(log_balanced_slope_bound) if ANGULAR_MODE == 2 else None,
        "R571_proof_applies_to_this_angular_mode": ANGULAR_MODE == 2,
        "those_bounds_exclude_numerical_ODE_error": True,
    }


def scaled_jets(u, state):
    """All returned quantities share the caller's logarithmic amplitude."""
    r, eps, g, elog, gp = coefficients(u)
    y, z = state
    yu = eps * z
    yuu = -g * yu - eps * y
    yuuu = -gp * yu - g * yuu - eps * elog * y - eps * yu
    ur = -u ** 2 / ELL
    urr = 2 * u ** 3 / ELL ** 2
    urrr = -6 * u ** 4 / ELL ** 3
    yr = yu * ur
    yrr = yuu * ur ** 2 + yu * urr
    yrrr = yuuu * ur ** 3 + 3 * yuu * ur * urr + yu * urrr
    j, mu = ANGULAR_MODE, ANGULAR_MODE ** 2
    f = r ** mu * y
    fr = mu * r ** (mu - 1) * y + r ** mu * yr
    frr = mu * (mu - 1) * r ** (mu - 2) * y + 2 * mu * r ** (mu - 1) * yr + r ** mu * yrr
    frrr = (mu * (mu - 1) * (mu - 2) * r ** (mu - 3) * y
            + 3 * mu * (mu - 1) * r ** (mu - 2) * yr
            + 3 * mu * r ** (mu - 1) * yrr + r ** mu * yrrr)
    delta = 1 / u
    angle = u + PHASE
    w = AMP * np.exp(-(2 - np.sin(angle)) / delta)
    wr = w * ((2 - np.sin(angle)) / delta ** 2 - np.cos(angle) / delta ** 3) / ELL
    a = w * (mu * f - r * fr) / (mu - 1)
    ar = w * fr
    arr = wr * fr + w * frr
    U = (mu - 1) / j * a / r
    Ur = (mu - 1) / j * (ar / r - a / r ** 2)
    Urr = (mu - 1) / j * (arr / r - 2 * ar / r ** 2 + 2 * a / r ** 3)
    V = -j * f / r
    Vr = -j * (fr / r - f / r ** 2)
    Vrr = -j * (frr / r - 2 * fr / r ** 2 + 2 * f / r ** 3)
    return np.asarray([f, fr, frr, frrr, a, ar, arr, U, Ur, Urr, V, Vr, Vrr])


def outward_profile(inner, rtol, atol, max_step, radial_nodes):
    alpha = inner["alpha_first"]
    inner_radius = RC + ELL / alpha
    radii = np.linspace(inner_radius, OUTER_RADIUS, radial_nodes)
    query_u = ELL / (radii - RC)
    query_u[0] = alpha
    last_u = float(query_u[-1])
    phase_breaks = np.pi / 2 + 2 * np.pi * np.arange(FIRST_PEAK + 1) - PHASE
    breaks = np.r_[alpha, np.sort(phase_breaks[(phase_breaks < alpha)
                                              & (phase_breaks > last_u)])[::-1], last_u]
    state = np.array([1.0, inner["z_at_alpha_first"]])
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
        "same_y_alpha_first_normalization_before_any_display_scaling": True,
        "z_alpha_first_difference": right["inner"]["z_at_alpha_first"] - left["inner"]["z_at_alpha_first"],
        "rho_first_plus_one_difference": right["inner"]["rho_first_plus_one"] - left["inner"]["rho_first_plus_one"],
        "outer_jet_difference_in_common_display_scale": difference[-1].tolist(),
        "outer_jet_relative_l2_difference": float(np.linalg.norm(difference[-1]) / denominator),
        "sampled_unit_T_C2_difference_max": float(np.max(np.abs(difference[:, c2_columns]))),
        "sampled_table_difference_max": float(np.max(np.abs(difference))),
        "comparison_is_not_a_certified_numerical_ODE_error_bound": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--M", type=int, default=25)
    parser.add_argument("--phase", type=float, default=0.0)
    parser.add_argument("--angular-mode", type=int, default=2)
    parser.add_argument("--radial-nodes", type=int, default=129)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.15)
    parser.add_argument("--tolerance-refinement", type=float, default=8.0)
    args = parser.parse_args()
    if args.radial_nodes < 3 or args.tolerance_refinement <= 1:
        raise ValueError("at least three output radii and an actual tolerance refinement are required")
    global PHASE, ANGULAR_MODE
    PHASE = args.phase
    ANGULAR_MODE = args.angular_mode
    if ANGULAR_MODE not in (2, 4, 6, 8):
        raise ValueError("only the proved mode 2 and explicit finite probes 4,6,8 are declared")
    if not 0 <= PHASE <= 2 * np.pi:
        raise ValueError("phase must belong to the declared interval [0,2pi]")
    started = time.monotonic()
    definition = {
        "schema": SCHEMA, "arguments": vars(args),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixed_profile": {"rc": RC, "ell": ELL, "A": AMP,
                          "w": "A*exp(-(2-sin(delta^-1+phase))/delta)", "phase": PHASE},
        "equation": "(w*f_r)_r-j^2*w_r*f/r=0",
        "angular_mode": ANGULAR_MODE, "first_peak_index": FIRST_PEAK,
        "R571_proof_applies_to_this_angular_mode": ANGULAR_MODE == 2,
        "transformed": "(p*y_u)_u+epsilon*p*y=0; f=r^(j^2)*y",
        "u_definition": "u=delta^-1; p=(A/ell)*u^2*r^(2*j^2)*exp(-u*(2-sin(u+phase)))",
        "epsilon_definition": "j^2*(j^2-1)*ell^2/(r^2*u^4)",
        "reference_R569_source_sha256": "e3a8f9255a4db33432dbe1692a0a34a03068ab1b396ab7c1e757de4c47a0bec7",
        "state": "y,z=y_u/epsilon; normalized y(alpha_first)=1 before outer extension",
        "terminal_indexing": "input M imposes rho_{M+1}=0 at alpha_{M+1}",
        "unit_T_seed": "delta_u=(j^2-1)*a/(j*r)*sin(j*theta), delta_v=-j*f/r*sin(j*theta)",
        "a_definition": "a=w*(j^2*f-r*f_r)/(j^2-1)",
        "radius_and_mean_height_first_variations": "zero",
        "fixed_metric": "(1+w^2)*dr^2+r^2*dtheta^2",
        "open_hat": "exact mathematical f,a,V all vanish to all orders at rc and are zero for r<=rc",
        "table_does_not_replace_the_infinite_inner_seed_by_a_finite_cutoff": True,
        "nonlinear_equal_metric_family_constructed": False,
        "README_completion_claim": False,
    }
    emit("R571_SEED_DEFINITION", definition)
    coarse = calculate(args.M, args.rtol, args.atol, args.max_step, args.radial_nodes)
    emit("R571_SEED_TRANSFER", {"run": "M_coarse", **coarse["inner"],
                               "nfev_outer": coarse["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": coarse["profile"]["outer_cauchy_log_norm"]})
    fine_rtol = args.rtol / args.tolerance_refinement
    fine_atol = args.atol / args.tolerance_refinement
    fine = calculate(args.M, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    emit("R571_SEED_TRANSFER", {"run": "M_finer_tolerance", **fine["inner"],
                               "nfev_outer": fine["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": fine["profile"]["outer_cauchy_log_norm"]})
    nextM = calculate(args.M + 1, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    emit("R571_SEED_TRANSFER", {"run": "M_plus_1_finer_tolerance", **nextM["inner"],
                               "nfev_outer": nextM["profile"]["nfev_outer"],
                               "outer_cauchy_log_norm": nextM["profile"]["outer_cauchy_log_norm"]})
    common_log_scale = fine["profile"]["outer_cauchy_log_norm"]
    values = display_profile(fine["profile"], common_log_scale)
    result = {
        "definition": definition,
        "common_display_log_scale_relative_to_y_alpha_first_equals_1": common_log_scale,
        "display_values_mean_exact_alpha_first_scale_times_exp_minus_common_log_scale": True,
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
        "inner_seed_remains_the_exact_R571_limit_not_a_new_zero_annulus": True,
        "linear_seed_only": True, "all_frequency_nonlinear_inverse_not_proved": True,
        "complete": False, "elapsed_seconds": time.monotonic() - started,
    }
    emit("R571_SEED_FINAL", result)
    raw = json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("R571_SEED_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()

