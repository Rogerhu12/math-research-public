#!/usr/bin/env python3
"""Floating periodic-orbit diagnostics of saved principal-map interpolants.

The results concern the named cubic interpolants only. They neither certify
the actual ray map nor exclude tangential periodic points without sign changes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline, PchipInterpolator
from scipy.optimize import brentq

from fourfold_circle_map_rotation import cubic_derivative_minimum


def check(spline, length, denominator, winding, probes):
    def lift(x):
        turns = np.floor(np.asarray(x)/length)
        return turns*length+spline(np.asarray(x)-turns*length)

    def iterate(x, derivative=False):
        y = np.asarray(x).copy()
        multiplier = np.ones_like(y)
        for _ in range(denominator):
            if derivative:
                multiplier *= spline(np.mod(y, length), nu=1)
            y = lift(y)
        return (y, multiplier) if derivative else y

    def residual(x):
        return iterate(x)-x-winding*length

    x = np.linspace(0., length, probes+1)
    y = residual(x)
    roots = []
    for left, right, yl, yr in zip(x[:-1], x[1:], y[:-1], y[1:]):
        if yl == 0:
            root = left
        elif yl*yr < 0:
            root = brentq(residual, left, right, xtol=5e-15)
        else:
            continue
        if not roots or root-roots[-1] > 1e-9:
            roots.append(float(root))
    multiplier = [float(iterate(root, True)[1]) for root in roots]
    return dict(
        derivative_minimum=cubic_derivative_minimum(spline),
        denominator=denominator, winding=winding, probes=probes+1,
        sampled_iterate_residual_range=[float(y.min()), float(y.max())],
        sign_change_roots=roots, multipliers=multiplier,
        attraction_counts=dict(attracting=sum(z < 1 for z in multiplier),
                               repelling=sum(z > 1 for z in multiplier)),
        interpolation_only=True, tangential_roots_not_excluded=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--denominator", type=int, required=True)
    parser.add_argument("--winding", type=int, required=True)
    parser.add_argument("--probes", type=int, default=16384)
    args = parser.parse_args()
    saved = json.loads(args.map.read_text())
    data = saved.get("principal_return", saved)
    length = data["angular_period"]
    x = np.r_[data["initial_angles"], length]
    y = np.r_[data["returned_angles"], data["returned_angles"][0]+length]
    d = data.get("angular_derivative", data.get("jacobian"))
    d = np.r_[d, d[0]]
    splines = dict(Hermite=CubicHermiteSpline(x, y, d),
                   PCHIP=PchipInterpolator(x, y))
    result = dict(
        kind="floating_high_period_check_of_interpolants_not_actual_operator_certificate",
        map_file=args.map.name,
        map_file_sha256=hashlib.sha256(args.map.read_bytes()).hexdigest(),
        source_checkpoint_sha256=saved.get("source_sha256", saved.get("sha256")),
        angular_period=length,
        interpolants={name:check(spline, length, args.denominator,
                                 args.winding, args.probes)
                      for name,spline in splines.items()},
        limitations=["no interval arithmetic or interpolation error bound",
                     "original radial reflection defect remains unpaid",
                     "periodic points belong to interpolants, not yet certified actual ODE points",
                     "no complete PDE scattering or exact flex conclusion"])
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({name:{key:value for key,value in entry.items()
                           if key not in ("sign_change_roots", "multipliers")}
                      for name,entry in result["interpolants"].items()}), flush=True)


if __name__ == "__main__":
    main()
