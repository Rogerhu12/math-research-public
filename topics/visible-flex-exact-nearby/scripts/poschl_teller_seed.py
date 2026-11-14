#!/usr/bin/env python3
"""Floating exploration of the exact R4 background, not a certificate.

The proof for every Fourier frequency is in R4.  This program samples the
background geometry and checks a bounded set of explicit spectral values.
It never labels these samples as rigorous bounds or an exact flexible family.
Requires numpy and scipy; all physical parameters are fixed by R4.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext, ROUND_FLOOR
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp


def spectral_diagnostic(max_mode: int) -> dict:
    with localcontext() as ctx:
        ctx.prec = 70
        mu = Decimal(2).sqrt()
        strength = Decimal(2) + mu / 3
        best = None
        for n in range(1, max_mode + 1):
            nd = Decimal(n)
            ell = ((1 + 4 * strength * nd * nd).sqrt() - 1) / 2
            center = int((ell - nd * mu).to_integral_value(rounding=ROUND_FLOOR))
            # Eigenvalues increase strictly in j<ell; only neighbors of the
            # zero crossing can minimize their absolute value.
            for j in sorted({0, max(0, center), max(0, center + 1)}):
                if Decimal(j) >= ell or (n == 3 and j == 0):
                    continue
                p = n * n - 3 * n * (2 * j + 1)
                q = 3 * j * (j + 1)
                d = (Decimal(p) * mu - Decimal(q)) / (
                    3 * (ell + nd * mu + Decimal(j) + 1)
                )
                eigenvalue = -d * (ell - Decimal(j) + nd * mu)
                if best is None or abs(eigenvalue) < best[0]:
                    best = (abs(eigenvalue), n, j, eigenvalue)
        assert best is not None
        return {
            "max_mode": max_mode,
            "decimal_precision": ctx.prec,
            "excluded_exact_kernel": {"n": 3, "j": 0},
            "minimum_absolute_discrete_eigenvalue": str(best[0]),
            "argmin_n": best[1],
            "argmin_j": best[2],
            "signed_eigenvalue": str(best[3]),
            "scope": "finite decimal diagnostic; not a proof of the all-mode gap",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xmax", type=float, default=10.0)
    parser.add_argument("--panels", type=int, default=10000)
    parser.add_argument("--max-mode", type=int, default=500)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if args.xmax <= 0 or args.panels < 2 or args.max_mode < 1:
        parser.error("positive xmax/max-mode and at least two panels are required")

    mu = np.sqrt(2.0)
    strength = 2.0 + mu / 3.0

    def rhs(x, state):
        h, hp, z, s = state
        q = 2.0 - strength / np.cosh(x) ** 2
        return [hp, q * h, 1.0 / h**2, np.sqrt(1.0 + hp**2) / h**2]

    solution = solve_ivp(
        rhs, (0.0, args.xmax), [1.0, 0.0, 0.0, 0.0],
        rtol=2e-12, atol=2e-14, dense_output=True,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    x = np.linspace(0.0, args.xmax, args.panels + 1)
    h, hp, z, arc = solution.sol(x)
    a = 1.0 / h
    p = np.sqrt(1.0 + hp**2)
    q = 2.0 - strength / np.cosh(x) ** 2
    k_angle = h / p
    k_radial = q * (h / p) ** 3
    support = (a + z * hp) / p
    radius = np.sqrt(a * a + z * z)
    kmax = float(max(np.abs(k_angle).max(), np.abs(k_radial).max()))
    rmax = float(radius.max())
    report = {
        "status": "floating diagnostics only; no rigorous geometry certificate",
        "object": "R4 rotational background, not a nonlinear flexible surface",
        "parameters": {"mu": "sqrt(2)", "A": "2+sqrt(2)/3"},
        "runtime": {"numpy": np.__version__, "scipy": scipy.__version__},
        "ode": {"method": "RK45", "rtol": 2e-12, "atol": 2e-14,
                "xmax": args.xmax, "panels": args.panels},
        "samples": {
            "h_min": float(h.min()),
            "half_height_at_xmax": float(z[-1]),
            "half_arc_length_at_xmax": float(arc[-1]),
            "enclosing_radius": rmax,
            "maximum_absolute_principal_curvature": kmax,
            "minimum_positive_support": float(support.min()),
            "uncertified_reach_proxy_over_ball_diameter":
                min(float(support.min()), 1.0 / kmax) / (2.0 * rmax),
        },
        "spectrum": spectral_diagnostic(args.max_mode),
        "missing": ["interval error control for geometry", "infinite x tail bounds",
                    "nonlinear exact isometry", "fixed open caps", "visible flex amplitude"],
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
