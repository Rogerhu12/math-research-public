#!/usr/bin/env python3
"""Floating geometric diagnostics of the R16 actual spline/integral maps.

This imports the existing candidate evaluator; it does not solve another ODE.
Finite body samples are neither a closed surface nor a global certificate.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

SOURCE = Path(__file__).with_name("poschl_teller_fourfold_series.py")
SPEC = importlib.util.spec_from_file_location("fourfold_series_geometry_source", SOURCE)
MODEL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODEL)


def extremum(values, x, theta, which="max"):
    flat = int(np.argmax(values) if which == "max" else np.argmin(values))
    at = np.unravel_index(flat, values.shape)
    return dict(value=float(values[at]), x=float(x[at[0]]),
                theta=float(theta[at[1]]))


def update(rec, name, values, x, theta, which="max"):
    new = extremum(values, x, theta, which)
    if (name not in rec or
            (which == "max" and new["value"] > rec[name]["value"]) or
            (which == "min" and new["value"] < rec[name]["value"])):
        rec[name] = new


def geometry(candidate, xgrid, theta, resolved_cut):
    all_rec, core_rec, outer_rec, terminal_rec = {}, {}, {}, {}
    terminal_start = max(resolved_cut, candidate["length"]-.25)
    for start in range(0, xgrid.size, 48):
        x = xgrid[start:start+48]
        f, fx, ft, fxx, fxt, ftt = MODEL.evaluate_candidate(
            candidate, x, theta, cartesian=True)
        normal_raw = np.cross(ft, fx)
        jac = np.linalg.norm(normal_raw, axis=-1)
        if np.any(jac == 0) or not np.all(np.isfinite(jac)):
            raise RuntimeError("sampled candidate has zero/nonfinite Jacobian")
        normal = normal_raw/jac[..., None]
        exx = np.sum(fx*fx, axis=-1)
        ext = np.sum(fx*ft, axis=-1)
        ett = np.sum(ft*ft, axis=-1)
        detg = jac*jac
        bxx = np.sum(normal*fxx, axis=-1)
        bxt = np.sum(normal*fxt, axis=-1)
        btt = np.sum(normal*ftt, axis=-1)
        trace = (bxx*ett-2*bxt*ext+btt*exx)/detg
        gauss = (bxx*btt-bxt*bxt)/detg
        discr = trace*trace-4*gauss
        root = np.sqrt(np.maximum(discr, 0))
        kabs = np.maximum(np.abs((trace+root)/2), np.abs((trace-root)/2))
        mean_xx = np.mean(exx, axis=1)[:, None]
        mean_tt = np.mean(ett, axis=1)[:, None]
        ra = (exx-mean_xx)/mean_xx
        rb = ext/np.sqrt(mean_xx*mean_tt)
        rc = (ett-mean_tt)/mean_tt
        center = (ra+rc)/2
        spread = np.sqrt(((ra-rc)/2)**2+rb*rb)
        metric_error = np.maximum(np.abs(center+spread), np.abs(center-spread))
        quantities = {
            "radius_max": (np.linalg.norm(f, axis=-1), "max"),
            "support_min": (np.sum(f*normal, axis=-1), "min"),
            "principal_curvature_abs_max": (kabs, "max"),
            "gauss_max": (gauss, "max"),
            "gauss_min": (gauss, "min"),
            "tangent_angle_sine_min": (jac/np.sqrt(exx*ett), "min"),
            "curvature_discriminant_min": (discr, "min"),
            "full_nonmean_metric_relative_max": (metric_error, "max"),
        }
        for name, (vals, which) in quantities.items():
            update(all_rec, name, vals, x, theta, which)
            mask = x <= resolved_cut
            if np.any(mask):
                update(core_rec, name, vals[mask], x[mask], theta, which)
            mask = x >= resolved_cut
            if np.any(mask):
                update(outer_rec, name, vals[mask], x[mask], theta, which)
            mask = x >= terminal_start
            if np.any(mask):
                update(terminal_rec, name, vals[mask], x[mask], theta, which)
    for rec in [all_rec, core_rec]:
        sig = rec["support_min"]["value"]
        kap = rec["principal_curvature_abs_max"]["value"]
        radius = rec["radius_max"]["value"]
        rec["twice_sampled_radius"] = 2*radius
        rec["reach_proxy_from_sample_extrema_not_bound"] = min(sig, 1/kap)
        rec["proxy_ratio_not_bound"] = min(sig, 1/kap)/(2*radius)
    return all_rec, core_rec, outer_rec, terminal_rec


def witness(series, candidate, epsilon, order):
    alpha = math.pi/4
    theta = np.array([0., -alpha])
    jets = MODEL.evaluate_candidate(candidate, np.array([0.]), theta, True)
    f, fx, ft = [a[0] for a in jets[:3]]
    rot = np.array([[math.cos(alpha), -math.sin(alpha), 0.],
                    [math.sin(alpha), math.cos(alpha), 0.], [0., 0., 1.]])
    p = f[0]
    q = rot@f[1]
    np0 = np.cross(ft[0], fx[0])
    nq0 = rot@np.cross(ft[1], fx[1])
    np0 /= np.linalg.norm(np0)
    nq0 /= np.linalg.norm(nq0)
    diff = p-q
    signed = float(diff@nq0)
    beta = float(np.linalg.norm(diff-signed*nq0))
    by_degree = {}
    for j in range(1, order+1):
        value = sum(float(c[0, 0]) for mode, (c, _) in
                    series["fields"].get(j, {}).items()
                    if mode % 8 == 4)
        by_degree[str(j)] = 2*epsilon**j*value
    return dict(
        phase_angle=alpha, point_phase_zero=p.tolist(),
        point_phase_pi_over_four=q.tolist(),
        normal_phase_zero=np0.tolist(), normal_phase_pi_over_four=nq0.tolist(),
        signed_normal_gap=signed, normal_gap_abs=abs(signed),
        tangential_defect=beta, point_distance=float(np.linalg.norm(diff)),
        parity_sum=sum(by_degree.values()), contributions_by_order=by_degree,
        meridian_vertical_derivative=[float(fx[0, 2]), float((rot@fx[1])[2])],
        angular_y_derivative=[float(ft[0, 1]), float((rot@ft[1])[1])],
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--series", type=Path, nargs="+", required=True)
    ap.add_argument("--epsilons", type=float, nargs="+", default=[.01, .05])
    ap.add_argument("--order", type=int, default=7)
    ap.add_argument("--samples", type=int, default=1201)
    ap.add_argument("--angles", type=int, default=192)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    report = dict(
        kind="floating_geometry_diagnostic_not_proof",
        evaluator=str(SOURCE.name),
        mean_height_representation="integral_of_quintic_even_slope",
        limitations=[
            "The input is a finite Robin BVP polynomial, not a closed fixed-cap surface.",
            "All derivatives are those of the same actual spline/integral candidate.",
            "No directed rounding, no global supremum or reach certificate.",
            "The reach proxies use sampled extrema and are not reach lower bounds.",
            "Twice sampled radius is not a certified diameter upper bound.",
            "Mean height is an integral of its slope spline; derivatives do not differentiate rounded polar heights.",
            "A normal gap is a rigorous Hausdorff witness only after a real global reach bound.",
            "No exact nonlinear isometry follows from these geometric diagnostics."],
        runs=[])
    theta = 2*np.pi*np.arange(args.angles)/args.angles
    for path in args.series:
        series = MODEL.load_series(path)
        order = min(args.order, series["parameters"]["order"])
        length = float(series["x"][-1])
        mu = float(series["parameters"]["mu"])
        xgrid = np.unique(np.r_[np.linspace(0., length, args.samples), series["x"]])
        resolved_cut = min(3., 10./mu, length)
        for epsilon in args.epsilons:
            candidate = MODEL.make_candidate(series, epsilon, order)
            all_rec, core_rec, outer_rec, terminal_rec = geometry(
                candidate, xgrid, theta, resolved_cut)
            wit = witness(series, candidate, epsilon, order)
            wit["gap_over_twice_sampled_radius_not_certificate"] = (
                wit["normal_gap_abs"]/all_rec["twice_sampled_radius"])
            rec = dict(series=path.name, parameters=series["parameters"],
                       epsilon=epsilon,
                       actual_epsilon=series["parameters"].get("actual_epsilon", epsilon),
                       order=order, samples=int(xgrid.size),
                       angles=args.angles, resolved_core_cut=resolved_cut,
                       entire_available_finite_body=all_rec,
                       central_resolved_range=core_rec,
                       outer_available_range=outer_rec,
                       terminal_range_start=max(resolved_cut, length-.25),
                       terminal_range=terminal_rec, waist_witness=wit)
            report["runs"].append(rec)
            print(json.dumps(dict(series=path.name, epsilon=epsilon,
                                  entire=all_rec, core=core_rec, witness=wit)),
                  flush=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")


if __name__ == "__main__":
    main()
