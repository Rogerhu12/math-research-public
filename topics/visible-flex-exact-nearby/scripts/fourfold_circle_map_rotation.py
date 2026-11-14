#!/usr/bin/env python3
"""Exploratory rotation and period-two checks of sampled principal maps.

Rotation is estimated by iterating degree-one lifts, never by averaging the
one-step displacement. Every conclusion concerns an explicitly constructed
interpolant until a separate map/ODE/interpolation error budget is proved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline, PchipInterpolator
from scipy.optimize import brentq


def cubic_derivative_minimum(spline):
    values = []
    for index, width in enumerate(np.diff(spline.x)):
        a, b, c = 3*spline.c[0, index], 2*spline.c[1, index], spline.c[2, index]
        values.extend((c, a*width*width+b*width+c))
        if a > 0:
            vertex = -b/(2*a)
            if 0 < vertex < width:
                values.append(a*vertex*vertex+b*vertex+c)
    return float(min(values))


def analyze(spline, period, iterations, probes):
    def lift(x):
        x = np.asarray(x)
        winding = np.floor(x/period)
        return winding*period+spline(x-winding*period)
    def derivative(x):
        return spline(np.mod(x, period), nu=1)
    minimum = cubic_derivative_minimum(spline)
    result = dict(interpolant_minimum_derivative=minimum,
                  interpolant_orientation_preserving=minimum > 0)
    if minimum <= 0:
        result["rotation_skipped"] = "interpolant is not an orientation-preserving diffeomorphism"
        return result
    seeds = np.arange(8)*period/8
    orbit = seeds.copy()
    for _ in range(iterations):
        orbit = lift(orbit)
    estimates = (orbit-seeds)/(iterations*period)
    intervals = np.stack((estimates-1/iterations, estimates+1/iterations), axis=-1)
    grid = np.linspace(0., period, probes+1)
    residual = lift(lift(grid))-grid-period
    roots = []
    for left, right, fl, fr in zip(grid[:-1], grid[1:], residual[:-1], residual[1:]):
        if fl == 0:
            root = left
        elif fl*fr < 0:
            root = brentq(lambda x: float(lift(lift(x))-x-period),
                          left, right, xtol=2e-14)
        else:
            continue
        if not roots or root-roots[-1] > 1e-9:
            roots.append(root)
    result.update(
        iteration_count=iterations, initial_seeds=seeds.tolist(),
        rotation_estimates=estimates.tolist(),
        floating_interpolant_translation_intervals=intervals.tolist(),
        intersection_of_these_intervals=[
            float(intervals[:, 0].max()), float(intervals[:, 1].min())],
        mean_estimate=float(np.mean(estimates)),
        period_two_residual_min=float(residual.min()),
        period_two_residual_max=float(residual.max()),
        period_two_residual_min_abs_grid=float(np.min(np.abs(residual))),
        period_two_sign_change_roots=roots,
        period_two_multipliers=[
            float(derivative(root)*derivative(lift(root))) for root in roots],
        period_two_scan_nodes=probes+1,
        interval_interpretation=(
            "For an exact increasing degree-one lift each n-step displacement/n differs "
            "from its translation number by at most period/n; numerical iteration and "
            "interpolation errors are not included here."),
        no_sign_change_is_not_a_tangent_root_exclusion=True)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--map", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--iterations", type=int, default=100000)
    p.add_argument("--probes", type=int, default=8192)
    args = p.parse_args()
    saved = json.loads(args.map.read_text())
    if saved.get("status", "complete") != "complete":
        raise ValueError("need a completed angular grid")
    data = saved.get("principal_return", saved)
    period = float(data["angular_period"])
    x = np.array(data["initial_angles"])
    y = np.array(data["returned_angles"])
    derivative = np.array(data.get("angular_derivative", data.get("jacobian")))
    if len(x) < 4 or x[0] != 0. or np.any(np.diff(x) <= 0):
        raise ValueError("need a full ordered periodic grid starting at zero")
    xx, yy, dd = np.r_[x, period], np.r_[y, y[0]+period], np.r_[derivative, derivative[0]]
    if np.any(np.diff(yy) <= 0):
        raise ValueError("sampled lift itself is not increasing")
    interpolants = [
        ("periodic_cubic_Hermite_with_actual_angular_derivatives", CubicHermiteSpline(xx, yy, dd)),
        ("monotone_PCHIP_lift", PchipInterpolator(xx, yy))]
    result = dict(
        kind="floating_interpolated_principal_rotation_exploration_not_true_map_certificate",
        map_file=args.map.name, map_file_sha256=hashlib.sha256(args.map.read_bytes()).hexdigest(),
        source_checkpoint_sha256=saved.get("source_sha256", saved.get("sha256")),
        angular_period=period, sample_count=len(x),
        interpolants={label:analyze(spline, period, args.iterations, args.probes)
                      for label, spline in interpolants},
        limitations=[
            "not a rotation-number certificate for the actual principal ODE",
            "interpolant differences expose angular under-resolution",
            "ordinary floating interpolation/root finding/iteration with no outward rounding",
            "period-two scan can miss tangential roots",
            "no phase-corrected PDE transfer, exact flex, or reach conclusion"])
    values = [item.get("mean_estimate") for item in result["interpolants"].values()]
    if all(value is not None for value in values):
        result["difference_between_interpolant_rotation_estimates"] = abs(values[0]-values[1])
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
