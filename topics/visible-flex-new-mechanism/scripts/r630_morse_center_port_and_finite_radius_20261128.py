#!/usr/bin/env python3
"""Actions-only exploration of the R630 Morse center.

The full-reference port integral uses exactly R630's left-regular radius.
The finite-radius alternatives use independent right-root initial data;
their reported port integrals are explicitly truncated core contributions,
not a flat-ended connector's port.  All numerical outputs are exploratory.
This file performs no GitHub mutation and contains no credentials.
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import platform
import subprocess
import time
from datetime import datetime, timezone

import mpmath as mp
import numpy as np
from scipy.integrate import quad, solve_ivp


def repository_head() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def full_reference_port(dps: int, cutoffs: list[float]) -> dict:
    """Integrate in t=exp(-X); t=0 is the infinite right reference end."""
    started = time.perf_counter()
    counts = {
        "radius_formula_evaluations": 0,
        "hyperu_calls": 0,
        "port_formula_evaluations": 0,
        "quadrature_callback_calls": 0,
    }
    mp.mp.dps = dps
    s = mp.sqrt(5)
    eta = mp.sqrt((36 * s - 27) / 20)
    big_b = (33 - 14 * s) / 20
    beta = mp.sqrt(eta**2 + big_b)
    a = beta - s / 2 + mp.mpf("0.5")
    b = 1 + 2 * beta
    alpha2 = s - mp.mpf("0.5")
    kappa3 = (3 * s - 3) / 2
    poly3_constant = 3 * s - 2

    @functools.lru_cache(maxsize=65536)
    def raw_radius(t):
        counts["radius_formula_evaluations"] += 1
        z = 2 * s * t
        counts["hyperu_calls"] += 1
        u0 = mp.hyperu(a, b, z)
        counts["hyperu_calls"] += 1
        u1 = mp.hyperu(a + 1, b + 1, z)
        psi = mp.exp(-z / 2) * z**beta * u0
        nu = eta + z / 2 - beta + a * z * u1 / u0
        return t ** (-eta) * psi, nu

    radius_scale, nu_at_one = raw_radius(mp.mpf(1))
    height_scale = 1 / nu_at_one
    f2_scale = mp.exp(-2 * s)
    f3_scale = mp.exp(-3 * s) * (poly3_constant - 6 * s)

    @functools.lru_cache(maxsize=65536)
    def port_integrands(t):
        counts["port_formula_evaluations"] += 1
        if t == 0:
            # Both limits vanish with positive powers of t.
            return mp.mpc(0)
        radius_raw, nu = raw_radius(t)
        radius = radius_raw / radius_scale
        w = height_scale * t ** (2 * eta) * nu * radius
        f = t ** (alpha2 - eta) * mp.exp(-2 * s * t) / f2_scale
        pref_g = t ** (kappa3 - eta) * mp.exp(-3 * s * t) / f3_scale
        poly = poly3_constant - 6 * s * t
        g = pref_g * poly
        fx = (eta - alpha2 + 2 * s * t) * f
        gx = pref_g * (
            (eta - kappa3 + 3 * s * t) * poly + 6 * s * t
        )
        fr = fx / (nu * radius)
        gr = gx / (nu * radius)
        # R628: J = J_without_w2 + w**2 * J_w2_coefficient.
        j0 = (
            radius * fr * gr
            - 9 * fr * g
            - 4 * f * gr
            + 12 * f * g / radius
        ) / 2
        j1 = (
            mp.mpf(19) / 6 * radius * fr * gr
            - mp.mpf(21) / 2 * fr * g
            - mp.mpf(14) / 3 * f * gr
            + 12 * f * g / radius
        ) / 2
        beta_without_w2 = -j0 * nu / (w * radius * t)
        beta_w2 = -j1 * w * nu / (radius * t)
        return mp.mpc(beta_without_w2, beta_w2)

    def counted_integrands(t):
        counts["quadrature_callback_calls"] += 1
        return port_integrands(t)

    knots = [
        mp.mpf("0"),
        mp.mpf("0.0001"),
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.2"),
        mp.mpf("0.35"),
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("4"),
    ]
    knots = sorted(set(knots + [mp.mpf(str(x)) for x in cutoffs]))
    rows = []
    for tmax_float in sorted(cutoffs):
        tmax = mp.mpf(str(tmax_float))
        points = [x for x in knots if x < tmax] + [tmax]
        value = mp.quad(counted_integrands, points, method="gauss-legendre")
        rows.append(
            {
                "t_upper_cutoff": str(tmax),
                "X_lower_cutoff": mp.nstr(-mp.log(tmax), dps),
                "X_upper_endpoint": "+infinity (reference only)",
                "beta_without_w2": mp.nstr(value.real, dps),
                "beta_w2_piece": mp.nstr(value.imag, dps),
                "beta_total_truncated": mp.nstr(value.real + value.imag, dps),
                "elapsed_seconds": time.perf_counter() - started,
                "actual_call_counts_cumulative": dict(counts),
            }
        )
    return {
        "dps": dps,
        "normalization": "r(0)=1; w(r(0))=1; f2(0)=f3(0)=1",
        "eta": mp.nstr(eta, dps),
        "B": mp.nstr(big_b, dps),
        "lambda": mp.nstr(height_scale, dps),
        "radius_scale": mp.nstr(radius_scale, dps),
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "actual_call_counts": counts,
        "scope": (
            "Ordinary high-precision quadrature, not interval certification. "
            "The omitted t>t_upper_cutoff tail is not included. "
            "This radius is the full-line left-regular reference only."
        ),
    }


def finite_radius_scan(epsilon: float) -> dict:
    """Right-type-root normalization r=1, r_X/r=epsilon, no global claim."""
    started = time.perf_counter()
    counts = {"rho_calls": 0, "ode_rhs_calls": 0, "core_port_calls": 0}
    s = np.sqrt(5.0)
    eta = np.sqrt((36 * s - 27) / 20)
    big_b = (33 - 14 * s) / 20
    rho_max = 5 / 4 - big_b
    kappa = eta - np.sqrt(eta**2 - rho_max)
    tminus = (1 - np.sqrt(1 - 4 * big_b / 5)) / 2
    tplus = (1 + np.sqrt(1 - 4 * big_b / 5)) / 2
    xl = -np.log(tplus)
    xr = -np.log(tminus)

    def rho(x):
        counts["rho_calls"] += 1
        t = np.exp(-x)
        return 5 * (t - t * t) - big_b

    def rhs(x, state):
        counts["ode_rhs_calls"] += 1
        log_r, nu, height = state
        radius = np.exp(log_r)
        return [
            nu,
            2 * eta * nu - nu * nu - rho(x),
            np.exp(-2 * eta * x) * (nu * radius) ** 2,
        ]

    def zero_velocity(x, state):
        return state[1]

    zero_velocity.terminal = True
    zero_velocity.direction = 0
    backward = solve_ivp(
        rhs,
        (xr, xl - 5),
        (0, epsilon, 0),
        method="DOP853",
        rtol=2e-12,
        atol=2e-14,
        events=zero_velocity,
        dense_output=True,
        max_step=0.02,
    )
    forward = solve_ivp(
        rhs,
        (xr, xr + 2),
        (0, epsilon, 0),
        method="DOP853",
        rtol=2e-12,
        atol=2e-14,
        dense_output=True,
        max_step=0.02,
    )
    left_state = backward.sol(xl)
    at_left_zero = (
        float(backward.t_events[0][0]) if len(backward.t_events[0]) else None
    )
    if at_left_zero is not None:
        # A fixed interior fraction avoids the zero of r_X.
        cut = xl + 0.8 * (at_left_zero - xl)
        left_positive_action = quad(
            lambda x: np.sqrt(max(0.0, -rho(x))),
            at_left_zero,
            xl,
            epsabs=1e-12,
            epsrel=1e-12,
        )[0]
    else:
        cut = float(backward.t[-1])
        left_positive_action = None

    # The shape derivative is rescaled so w=1 at the right type root.
    height_scale = np.exp(2 * eta * xr) / epsilon
    alpha2 = s - 0.5
    kappa3 = (3 * s - 3) / 2
    m3 = 3 * s - 2
    t_root = np.exp(-xr)
    f2_scale = t_root ** (alpha2 - eta) * np.exp(-2 * s * t_root)
    f3_scale = (
        t_root ** (kappa3 - eta)
        * np.exp(-3 * s * t_root)
        * (m3 - 6 * s * t_root)
    )

    def core_port_density(x):
        counts["core_port_calls"] += 1
        log_r, nu, _ = backward.sol(x) if x <= xr else forward.sol(x)
        radius = np.exp(log_r)
        t = np.exp(-x)
        w = height_scale * np.exp(-2 * eta * x) * nu * radius
        f = t ** (alpha2 - eta) * np.exp(-2 * s * t) / f2_scale
        pref_g = t ** (kappa3 - eta) * np.exp(-3 * s * t) / f3_scale
        poly = m3 - 6 * s * t
        g = pref_g * poly
        fx = (eta - alpha2 + 2 * s * t) * f
        gx = pref_g * ((eta - kappa3 + 3 * s * t) * poly + 6 * s * t)
        fr, gr = fx / (nu * radius), gx / (nu * radius)
        j0 = (radius * fr * gr - 9 * fr * g - 4 * f * gr + 12 * f * g / radius) / 2
        j1 = (
            (19 / 6) * radius * fr * gr
            - (21 / 2) * fr * g
            - (14 / 3) * f * gr
            + 12 * f * g / radius
        ) / 2
        return -(j0 + w * w * j1) * nu / (w * radius)

    core_rows = []
    for right_extra in (0.0, 0.25, 0.5, 1.0):
        endpoint = xr + right_extra
        rs, nus, hs = forward.sol(endpoint)
        ls, lnu, lh = backward.sol(cut)
        port = quad(
            core_port_density,
            cut,
            endpoint,
            epsabs=1e-8,
            epsrel=1e-9,
            points=[xl, xr] if endpoint > xr else [xl],
            limit=300,
        )
        core_rows.append(
            {
                "X_left_cut": float(cut),
                "X_right_cut": float(endpoint),
                "r_left": float(np.exp(ls)),
                "r_right": float(np.exp(rs)),
                "nu_left": float(lnu),
                "nu_right": float(nus),
                "center_height_drop": float(height_scale * (hs - lh)),
                "beta_core_contribution_only": float(port[0]),
                "quadrature_error_estimate": float(port[1]),
            }
        )
    return {
        "epsilon_at_right_type_root": epsilon,
        "kappa_invariant_upper_bound": float(kappa),
        "analytic_invariant_interval_applies": bool(0 < epsilon < kappa),
        "left_type_X": float(xl),
        "right_type_X": float(xr),
        "negative_component_radius_ratio": float(np.exp(-left_state[0])),
        "analytic_ratio_upper_bound": float(np.exp(kappa * (xr - xl))),
        "nu_at_left_type": float(left_state[1]),
        "first_left_zero_of_nu_X": at_left_zero,
        "available_left_positive_action_before_zero": left_positive_action,
        "backward_solver_success": bool(backward.success),
        "forward_solver_success": bool(forward.success),
        "normalization": "r(X_R)=1; w(r(X_R))=1; f2(X_R)=f3(X_R)=1",
        "core_rows": core_rows,
        "elapsed_seconds": time.perf_counter() - started,
        "actual_call_counts": counts,
        "backward_scipy_nfev": int(backward.nfev),
        "forward_scipy_nfev": int(forward.nfev),
        "scope": (
            "Finite radial branch only. The reported beta is an incomplete "
            "core integral: the modes do not have flat-end boundary conditions, "
            "and no boundary connector or global inverse is inferred."
        ),
    }


def main() -> None:
    if not (
        os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY", "").lower()
        == "rogerhu12/math-research-public"
        and os.environ.get("GITHUB_RUN_ID")
    ):
        raise SystemExit(
            "Scientific calculation is authorized only inside the public "
            "Rogerhu12/math-research-public GitHub Actions runner."
        )
    started = time.perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", nargs="+", type=int, default=[50, 70])
    parser.add_argument("--tmax", nargs="+", type=float, default=[8, 12])
    parser.add_argument(
        "--epsilon", nargs="+", type=float, default=[0.005, 0.02, 0.1, 0.2]
    )
    parser.add_argument("--skip-reference", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            {
                "kind": "provenance",
                "utc": datetime.now(timezone.utc).isoformat(),
                "git_head": repository_head(),
                "python": platform.python_version(),
                "calculation_location_required": "public GitHub Actions",
                "github_run_id": os.environ["GITHUB_RUN_ID"],
                "github_job": os.environ.get("GITHUB_JOB"),
                "certified": False,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    for epsilon in args.epsilon:
        print(
            json.dumps(
                {"kind": "finite_radius_scan", **finite_radius_scan(epsilon)},
                sort_keys=True,
            ),
            flush=True,
        )
    if not args.skip_reference:
        for dps in args.dps:
            print(
                json.dumps(
                    {"kind": "full_reference_port", **full_reference_port(dps, args.tmax)},
                    sort_keys=True,
                ),
                flush=True,
            )
    print(
        json.dumps(
            {"kind": "completed", "elapsed_seconds": time.perf_counter() - started},
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
