#!/usr/bin/env python3
"""Re-evaluate C signs for one already published, frozen geometric candidate.

All geometry quadratures run in the public repository Actions.  Sampled omega
bounds and floating-point quadrature are diagnostics, not continuous interval
certificates.  No tilt, normalization, or geometric control is re-optimized.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

import literature_closed_codesign as closed
from literature_base_codesign import NAMES


def C_coefficients(c):
    return np.array([c[5], c[6]+c[7], -c[0]/4+c[8]+c[9],
                     c[10]-c[1]/4, -c[2]/4])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).parents[1]/
                        "notes/actions-43591099281-1-closed_design/nine-coefficients-closed-design.json")
    parser.add_argument("--design-index", type=int, default=1)
    parser.add_argument("--stage", choices=["initial", "final"], default="initial")
    parser.add_argument("--theta-n", type=int, nargs="+", default=[768, 1536, 3072, 6144])
    parser.add_argument("--xi", type=float, nargs="+", default=[10., 25.])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--developer-check", action="store_true")
    args = parser.parse_args()
    if args.developer_check:
        # A fixed synthetic extraction identity; no geometry is evaluated.
        c = np.arange(11, dtype=float)
        actual = C_coefficients(c)
        expected = np.array([5., 13., 17., 9.75, -.5])
        if not np.array_equal(actual, expected):
            raise AssertionError((actual, expected))
        report = dict(kind="synthetic_coefficient_interface_check",
                      no_geometry_evaluated=True, maximum_error=0.)
    else:
        if os.environ.get("GITHUB_ACTIONS") != "true" or \
                os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
            raise SystemExit("Run geometry diagnostics in the public repository Actions.")
        raw = args.input.read_bytes()
        source = json.loads(raw)
        design = source["designs"][args.design_index]
        parameters = design[args.stage+"_parameters"]
        q, modes = design["q"], source["arguments"]["modes"]
        if args.stage == "initial":
            frozen = {key: design["initial"][key] for key in ["tilt", "normalization"]}
        else:
            frozen = dict(design["frozen_validation_data"])
        validations = []
        for n in args.theta_n:
            g = closed.geometry(parameters, q, modes, n, frozen=frozen)
            c = g["coefficients"]
            cp = C_coefficients(c)
            om_min, om_max = float(np.min(g["omega"])), float(np.max(g["omega"]))
            roots = []
            for root in np.polynomial.polynomial.polyroots(cp):
                numerical_real = bool(abs(root.imag) <= 1e-8*max(1., abs(root.real)))
                xi = float(root.real)
                region = "complex"
                if numerical_real:
                    region = ("positive_u" if xi+om_min > 0 else
                              "negative_u" if xi+om_max < 0 else "crosses_sampled_pole_range")
                roots.append(dict(real=xi, imag=float(root.imag),
                                  numerical_real=numerical_real,
                                  sampled_region=region,
                                  derivative_real=float(np.polynomial.polynomial.polyval(
                                      xi, np.polynomial.polynomial.polyder(cp)))))
            values = []
            h = np.sqrt(g["v"])
            for xi in args.xi:
                z = xi+g["omega"]
                value = float(np.polynomial.polynomial.polyval(xi, cp))
                region = ("positive_u" if np.min(z) > 0 else
                          "negative_u" if np.max(z) < 0 else "crosses_sampled_pole_range")
                u_range = None
                if region != "crosses_sampled_pole_range":
                    u = h/z
                    u_range = [float(np.min(u)), float(np.max(u))]
                values.append(dict(xi=xi, C_value=value, sampled_region=region,
                                   z_sample_range=[float(np.min(z)), float(np.max(z))],
                                   u_sample_range=u_range))
            # c has the original eleven reporting slots:
            # p0,p1,p2,q0,q1,r0,r1,s0,s1,t0,t1.
            d_identity = float(c[0]/2+c[8]-2*c[9])
            validations.append(dict(
                theta_n=n, C_ascending_coefficients=cp.tolist(),
                C_roots=roots, evaluation_points=values,
                omega_sample_range=[om_min, om_max],
                period_coefficients=dict(zip(NAMES, map(float, c))),
                D_identity_residual=d_identity,
                polynomial_identity_error=g["polynomial_identity_error"],
                curve_closure_vector=g["closure"].tolist(),
                curve_closure_over_length=float(np.linalg.norm(g["closure"])/g["length"]),
                asymptotic_half_period=g["asymptotic_half_period"]))
        report = dict(
            schema="literature-physical-C-sign-frozen-audit-v1",
            source_commit=os.environ.get("GITHUB_SHA", ""),
            source_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            origin_path=str(args.input),
            origin_file_sha256=hashlib.sha256(raw).hexdigest(),
            design_index=args.design_index, source_stage=args.stage, q=q, modes=modes,
            frozen_parameters=parameters, frozen_tilt_and_normalization=frozen,
            all_quadratures_evaluate_same_frozen_geometric_candidate=True,
            validations=validations,
            continuous_C_sign_certified=False, continuous_omega_bound_certified=False,
            real_C_root_count_on_physical_component_proved=False,
            geometric_base_embedded_proved=False, reach_lower_certified=False,
            global_profile_constructed=False, finite_flex_proved=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    body = json.dumps(report, indent=2, allow_nan=False)+"\n"
    args.out.write_text(body)
    print(body)


if __name__ == "__main__":
    main()
