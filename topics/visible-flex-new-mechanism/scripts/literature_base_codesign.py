#!/usr/bin/env python3
"""Design the eleven R5 period coefficients, without claiming a finite flex.

All optimization is restricted to this public repository's GitHub Actions.
The B indicatrix and log speed have exact q-fold and reflection symmetries.
Reflection makes the asymptotic period vanish; axial curve closure remains an
explicit equation. A mean-subtracted primitive never substitutes for closure.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares

import literature_band_seed as seed
from literature_band_second_order import polynomial_period_operator


NAMES = ["p0", "p1", "p2", "q0", "q1", "r0", "r1", "s0", "s1", "t0", "t1"]


def extract_coefficients(values):
    """Values at xi=-1,0,1,2; extraction uses only -1,0,1 and identities."""
    a0, a1, a2, b0, b1, b2 = np.asarray(values)
    p0 = a1[1]
    p1 = (a1[2] - a1[0]) / 2
    p2 = (a1[2] + a1[0] - 2 * a1[1]) / 2
    return np.array([p0, p1, p2, a2[1], (a2[2] - a2[0]) / 2 + p2 / 2,
                     b0[1], (b0[2] - b0[0]) / 2,
                     b1[1], (b1[2] - b1[0]) / 2,
                     b2[1], (b2[2] - b2[0]) / 2])


def reconstruct_coefficients(c, x):
    p0, p1, p2, q0, q1, r0, r1, s0, s1, t0, t1 = c
    return np.array([-p1 / 2 - p2 * x,
                     p0 + p1 * x + p2 * x * x,
                     q0 + q1 * x + (t1 - p1 / 2) * x * x - p2 * x**3 / 2,
                     r0 + r1 * x - p0 * x * x / 4,
                     s0 + s1 * x - p1 * x * x / 4,
                     t0 + t1 * x - p2 * x * x / 4])


def geometry(parameters, q, n, fixed_normalization=None):
    a, b = parameters[:2]
    d = seed.spherical_data(q, a, "symmetric", b, n)
    theta = d["theta"]
    frequency = q * np.arange(1, len(parameters) - 1)
    cs = np.cos(theta[:, None] * frequency[None, :])
    sn = np.sin(theta[:, None] * frequency[None, :])
    logh = cs @ parameters[2:]
    logh_theta = -(sn * frequency[None, :]) @ parameters[2:]
    raw_v = np.exp(2 * logh)
    normalization = (float(np.mean(raw_v * d["sphere_speed"]) / np.mean(d["sphere_speed"]))
                     if fixed_normalization is None else fixed_normalization)
    v = raw_v / normalization
    vp = 2 * v * logh_theta
    om_theta = d["kappa_theta"] / (2 * np.sqrt(v))
    om = seed.periodic_primitive(om_theta[:, None])[:, 0]
    period = float(2 * np.pi * np.mean(om_theta))
    closure = 2 * np.pi * np.mean(v[:, None] * d["raw"], axis=0)
    curve_length = float(2 * np.pi * np.mean(v * d["sphere_speed"]))
    xi = np.array([-1., 0., 1., 2.])
    values = np.array(polynomial_period_operator(d, v, vp, om, xi))
    coeff = extract_coefficients(values)
    identity_error = float(np.max(np.abs(values - reconstruct_coefficients(coeff, xi))))
    return dict(data=d, v=v, vp=vp, omega=om, period=period, closure=closure,
                length=curve_length, normalization=normalization, coeff=coeff,
                identity_error=identity_error, centered_logh=logh - .5 * np.log(normalization))


def initial_parameters(q, a, b, modes, n):
    d = seed.spherical_data(q, a, "symmetric", b, n)
    parameters = argparse.Namespace(q=q, a=a, b=b, c=1 / b, kind="symmetric")
    v, _ = seed.speed_data(parameters, d, None)
    logh = .5 * np.log(v)
    coefficients = [float(2 * np.mean(logh * np.cos(j * q * d["theta"])))
                    for j in range(1, modes + 1)]
    return np.r_[a, b, np.clip(coefficients, -.39, .39)]


def diagnostics(g, n, scales, parameters, q):
    # These are finite samples, never lower bounds for reach.
    alpha = seed.periodic_primitive(g["v"][:, None] * g["data"]["raw"])
    points = alpha[::max(1, n // 768)]
    diameter = seed.sampled_diameter(points)
    curvature_at_center = float(np.max(1 / g["v"]))
    return dict(theta_n=n, period_coefficients=dict(zip(NAMES, map(float, g["coeff"]))),
                scaled_coefficient_l2=float(np.linalg.norm(g["coeff"] / scales)),
                scaled_coefficient_max=float(np.max(np.abs(g["coeff"] / scales))),
                polynomial_identity_max_error=g["identity_error"],
                curve_closure_vector=g["closure"].tolist(),
                relative_curve_closure=float(np.linalg.norm(g["closure"]) / g["length"]),
                asymptotic_half_period_removed=g["period"],
                speed_min=float(np.min(g["v"])), speed_max=float(np.max(g["v"])),
                speed_contrast=float(np.max(g["v"]) / np.min(g["v"])),
                projected_periodic_centerline_diameter=diameter,
                formal_band_radius_over_projected_diameter=1 / (curvature_at_center * diameter),
                geometry_is_only_a_projected_diagnostic_when_closure_is_nonzero=True,
                removed_curve_derivative_mean=(g["closure"] / (2 * np.pi)).tolist(),
                q=q, a=float(parameters[0]), b=float(parameters[1]),
                normalization=g["normalization"], not_a_reach_certificate=True)


def one_design(args, q, a, b):
    initial = initial_parameters(q, a, b, args.modes, args.theta_n)
    initial_g = geometry(initial, q, args.theta_n)
    scales = np.maximum(1., np.abs(initial_g["coeff"]))
    def residual(parameters):
        g = geometry(parameters, q, args.theta_n)
        # Bounds on log speed avoid achieving a small normalized residual by
        # severe concentration. All coefficient scales remain frozen.
        sample = g["centered_logh"][::max(1, args.theta_n // 96)]
        concentration = np.maximum(np.abs(sample) - args.logh_bound, 0)
        return np.r_[g["coeff"] / scales,
                     20 * g["closure"][2] / g["length"], 10 * concentration]
    start = time.monotonic()
    fit = least_squares(residual, initial, bounds=(np.r_[.08, .8, np.full(args.modes, -.4)],
                                                  np.r_[.85, 1.55, np.full(args.modes, .4)]),
                        max_nfev=args.max_nfev, ftol=1e-11, xtol=1e-11, gtol=1e-10,
                        x_scale="jac", diff_step=2e-5)
    final_g = geometry(fit.x, q, args.theta_n)
    frozen_normalization = final_g["normalization"]
    validation = []
    for n in args.validation_n:
        g = geometry(fit.x, q, n, frozen_normalization)
        validation.append(diagnostics(g, n, scales, fit.x, q))
    return dict(status="finite_base_design_not_a_surface_flex", q=q,
                initial_parameters=initial.tolist(), final_parameters=fit.x.tolist(),
                coefficient_scales=scales.tolist(), frozen_speed_normalization=frozen_normalization,
                solver=dict(success=bool(fit.success), message=str(fit.message), nfev=int(fit.nfev),
                            optimality=float(fit.optimality), elapsed_seconds=time.monotonic() - start,
                            initial_residual_l2=float(np.linalg.norm(residual(initial))),
                            final_residual_l2=float(np.linalg.norm(fit.fun))),
                initial=diagnostics(initial_g, args.theta_n, scales, initial, q),
                validation=validation, exact_closure_proved=False, all_coefficients_zero_proved=False,
                finite_isometric_path_proved=False, task_complete=False)


def developer_check():
    coefficients = np.arange(1., 12.) / 7
    xi = np.array([-1., 0., 1., 2.])
    recovered = extract_coefficients(reconstruct_coefficients(coefficients, xi))
    error = float(np.max(np.abs(recovered - coefficients)))
    if error > 1e-12:
        raise AssertionError(error)
    # A round spherical indicatrix has constant kappa and h; all integrals are
    # constant and need no research solve to check signs and coefficient maps.
    n = 16
    theta = 2 * np.pi * np.arange(n) / n
    data = dict(theta=theta, sphere_speed=np.ones(n), kappa=np.ones(n),
                kappa_theta=np.zeros(n))
    actual = np.array(polynomial_period_operator(data, np.ones(n), np.zeros(n),
                                                 np.zeros(n), xi))
    err = float(np.max(np.abs(actual - reconstruct_coefficients(extract_coefficients(actual), xi))))
    if err > 1e-11:
        raise AssertionError(err)
    print(json.dumps(dict(developer_check=True, coefficient_roundtrip_max=error,
                          constant_geometry_identity_max=err), allow_nan=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modes", type=int, default=12)
    parser.add_argument("--theta-n", type=int, default=768)
    parser.add_argument("--validation-n", type=int, nargs="+", default=[768, 1536, 3072])
    parser.add_argument("--max-nfev", type=int, default=350)
    parser.add_argument("--logh-bound", type=float, default=.8)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--developer-check", action="store_true")
    args = parser.parse_args()
    if args.developer_check:
        developer_check()
        return
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Run optimization in this public repository's own GitHub Actions.")
    if args.out is None:
        parser.error("--out is required")
    output = dict(status="finite_base_codesign", profile_space="R5 four even poly4 profiles",
                  physical_parameter_validation=True, exact_isometry_proved=False,
                  task_complete=False, arguments=vars(args) | {"out": str(args.out)}, designs=[],
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    for q, a, b in [(3, .35, 1.1), (2, .60, 1.2), (4, .35, 1.1)]:
        result = one_design(args, q, a, b)
        output["designs"].append(result)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
        print(json.dumps(dict(q=q, solver=result["solver"], final=result["validation"][-1]), allow_nan=False))


if __name__ == "__main__":
    main()
