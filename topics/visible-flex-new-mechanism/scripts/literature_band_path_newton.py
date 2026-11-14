#!/usr/bin/env python3
"""Fixed-g nonlinear path slices from the three-moment profile pair.

Target g_epsilon is fixed throughout all phases.  The radial amplitude is free;
only the phase of the L2 projection to span(Yf,Yg) is prescribed.  General C2
zero-boundary correction fields supply all three ambient components.  A failed
finite-dimensional solve is not a nonexistence theorem.  Run in public Actions.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre as leg
from scipy.linalg import cholesky, qr, solve_triangular
from scipy.optimize import least_squares

import literature_band_kernel as kernel
import literature_band_second_order as second


def grid_model(args, prepared, nt, nx):
    parameters, amplitude, reference, f, g, common_scale, _ = prepared
    d, v, vp, om = kernel.sample_geometry(parameters, amplitude, nt)
    y, yw = leg.leggauss(nx)
    halfwidth = (reference["profile_right"] - reference["profile_left"]) / 2
    xi = (reference["profile_right"] + reference["profile_left"]) / 2 + halfwidth * y
    u = np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])
    xi_s = ((vp / d["sphere_speed"])[:, None] / u
            - (d["kappa_theta"] / d["sphere_speed"])[:, None]) / (2 * np.sqrt(v)[:, None])
    xi_u = -np.sqrt(v)[:, None] / u**2
    pair = second.field_pair(d, v, vp, om, u, reference, f, g, common_scale)
    (Yf, Yg), (Yfs, Ygs), (Yfu, Ygu) = pair
    psi, ps, pu = kernel.basis(d, y, halfwidth, args.modes, args.degree, xi_s, xi_u)
    kappa = np.repeat(d["kappa"], nx)[:, None]
    zero = np.zeros_like(psi)
    fields = np.concatenate((np.stack((psi, zero, zero), axis=1),
                             np.stack((zero, psi, zero), axis=1),
                             np.stack((zero, zero, psi), axis=1),
                             Yf[:, :, None], Yg[:, :, None]), axis=2)
    fields_s = np.concatenate((np.stack((ps, kappa * psi, zero), axis=1),
                               np.stack((-kappa * psi, ps, -psi), axis=1),
                               np.stack((zero, psi, ps), axis=1),
                               Yfs[:, :, None], Ygs[:, :, None]), axis=2)
    fields_u = np.concatenate((np.stack((pu, zero, zero), axis=1),
                               np.stack((zero, pu, zero), axis=1),
                               np.stack((zero, zero, pu), axis=1),
                               Yfu[:, :, None], Ygu[:, :, None]), axis=2)
    w = (v[:, None] - d["kappa"][:, None] * u).ravel()
    Xs = np.column_stack((w, np.zeros_like(w), -u.ravel()))
    Xu = np.column_stack((np.zeros_like(w), np.ones_like(w), np.zeros_like(w)))
    target_s, target_u = Xs + args.epsilon * Yfs, Xu + args.epsilon * Yfu
    E = np.sum(target_s * target_s, axis=1)
    F = np.sum(target_s * target_u, axis=1)
    G = np.sum(target_u * target_u, axis=1)
    det = E * G - F * F
    u_jacobian = halfwidth * np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])**2
    area = (2 * np.pi / nt * np.repeat(d["sphere_speed"], nx)
            * np.tile(yw, nt) * u_jacobian.ravel() * np.sqrt(det))
    return dict(data=d, u=u, xi_s=xi_s, xi_u=xi_u, y=y, yw=yw,
                xi_halfwidth=halfwidth, fields=fields, fields_s=fields_s,
                fields_u=fields_u, Xs=Xs, Xu=Xu, E=E, F=F, G=G, det=det, area=area)


def metric_error(model, Fs, Fu):
    E, F, G, determinant = model["E"], model["F"], model["G"], model["det"]
    dE = np.sum(Fs * Fs, axis=1) - E
    dF = np.sum(Fs * Fu, axis=1) - F
    dG = np.sum(Fu * Fu, axis=1) - G
    return np.stack((dE / E,
                     np.sqrt(2) * (E * dF - F * dE) / (E * np.sqrt(determinant)),
                     (F * F * dE - 2 * E * F * dF + E * E * dG) / (E * determinant)), axis=1)


def slice_solve(args, model, C_perp, phase, initial, check_jacobian=False):
    columns = model["fields"].shape[2]
    direction = np.zeros(columns)
    direction[-2], direction[-1] = np.cos(phase), np.sin(phase)
    C = np.column_stack((direction, C_perp))
    ds = np.einsum("nik,kj->nij", model["fields_s"], C)
    du = np.einsum("nik,kj->nij", model["fields_u"], C)
    sqrt_weight = np.sqrt(model["area"] / np.sum(model["area"]))
    E, F, determinant = model["E"], model["F"], model["det"]
    def positions(x):
        return (model["Xs"] + np.einsum("nik,k->ni", ds, x),
                model["Xu"] + np.einsum("nik,k->ni", du, x))
    def residual(x):
        Fs, Fu = positions(x)
        return (sqrt_weight[:, None] * metric_error(model, Fs, Fu)).ravel()
    def jacobian(x):
        Fs, Fu = positions(x)
        dE = 2 * np.einsum("ni,nik->nk", Fs, ds)
        dF = np.einsum("ni,nik->nk", Fs, du) + np.einsum("ni,nik->nk", Fu, ds)
        dG = 2 * np.einsum("ni,nik->nk", Fu, du)
        j1 = dE / E[:, None]
        j2 = np.sqrt(2) * (E[:, None] * dF - F[:, None] * dE) / (E * np.sqrt(determinant))[:, None]
        j3 = (F[:, None]**2 * dE - 2 * (E * F)[:, None] * dF + E[:, None]**2 * dG) / (E * determinant)[:, None]
        return (sqrt_weight[:, None, None] * np.stack((j1, j2, j3), axis=1)).reshape(-1, len(x))
    derivative_check = None
    if check_jacobian:
        # Work at a nonzero correction, separate from the solver initial value.
        # A unit direction changes the tangent differential by at most one in
        # the target metric's orthonormal basis.  This fixes a meaningful step
        # scale despite very different raw amplitude/correction coordinates.
        def normalize_direction(direction):
            delta_s = np.einsum("nik,k->ni", ds, direction)
            delta_u = np.einsum("nik,k->ni", du, direction)
            first = delta_s / np.sqrt(E)[:, None]
            second = (E[:, None] * delta_u - F[:, None] * delta_s) / np.sqrt(E * determinant)[:, None]
            size = np.max(np.sqrt(np.sum(first * first + second * second, axis=1)))
            return direction / max(float(size), np.finfo(float).tiny)
        rng = np.random.default_rng(20261114)
        correction_direction = rng.standard_normal(len(initial))
        correction_direction[0] = 0
        correction_direction = normalize_direction(correction_direction)
        radial_direction = np.zeros(len(initial))
        radial_direction[0] = 1
        radial_direction = normalize_direction(radial_direction)
        probe = initial + .01 * correction_direction
        analytic = jacobian(probe)
        checks = []
        for name, direction in (("radial", radial_direction),
                                ("nonzero_correction", correction_direction),
                                ("mixed", normalize_direction(radial_direction + correction_direction))):
            expected = analytic @ direction
            trials = []
            for step in (1e-4, 1e-5, 1e-6):
                numerical = (residual(probe + step * direction) - residual(probe - step * direction)) / (2 * step)
                difference = numerical - expected
                trials.append(dict(step=step, max_abs_error=float(np.max(np.abs(difference))),
                    relative_l2_error=float(np.linalg.norm(difference) / max(np.linalg.norm(expected), 1e-30)),
                    relative_max_error=float(np.max(np.abs(difference)) / max(np.max(np.abs(expected)), 1e-30))))
            checks.append(dict(direction=name, analytic_l2_norm=float(np.linalg.norm(expected)), trials=trials))
        derivative_check = dict(method="Central differences at initial plus a 0.01 normalized correction; solver initial is unchanged",
            direction_scale="Maximum target-orthonormal tangent differential norm is one",
            random_seed=20261114, checks=checks,
            passed=bool(all(min(t["relative_l2_error"] for t in check["trials"]) < 1e-7 for check in checks)))
    lower = np.full(len(initial), -np.inf)
    upper = np.full(len(initial), np.inf)
    lower[0], upper[0] = args.epsilon / 10, args.epsilon * 10
    fit = least_squares(residual, initial, jac=jacobian, bounds=(lower, upper),
                        max_nfev=args.max_nfev, xtol=1e-11, ftol=1e-11, gtol=1e-11,
                        method="trf", tr_solver="exact")
    coeff = C @ fit.x
    Fs, Fu = positions(fit.x)
    metric = metric_error(model, Fs, Fu)
    return fit.x, coeff, dict(phase_over_pi=float(phase / np.pi), solver_success=bool(fit.success),
                              solver_status=int(fit.status), solver_message=fit.message,
                              evaluations=int(fit.nfev), optimality=float(fit.optimality),
                              radial_amplitude=float(fit.x[0]), amplitude_over_epsilon=float(fit.x[0] / args.epsilon),
                              training_max_relative_metric_frobenius=float(np.max(np.linalg.norm(metric, axis=1))),
                              training_area_rms_relative_metric=float(np.sqrt(2 * fit.cost)),
                              amplitude_bound_active=bool(fit.active_mask[0] != 0),
                              jacobian_check=derivative_check)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kind", choices=["curvature", "symmetric"], default="curvature")
    p.add_argument("--profile-kind", choices=["bump", "polynomial"], default="bump")
    p.add_argument("--profile-power", type=int, default=4)
    p.add_argument("--q", type=int, default=3)
    p.add_argument("--a", type=float)
    p.add_argument("--b", type=float, default=.85)
    p.add_argument("--c", type=float, default=1.7)
    p.add_argument("--power", type=float, default=1)
    p.add_argument("--center", type=float, default=-3)
    p.add_argument("--sigma", type=float, default=1.5)
    p.add_argument("--delta", type=float, default=.3)
    p.add_argument("--profile-count", type=int, default=4)
    p.add_argument("--theta-n", type=int, default=192)
    p.add_argument("--xi-n", type=int, default=64)
    p.add_argument("--modes", type=int, default=3)
    p.add_argument("--degree", type=int, default=8)
    p.add_argument("--epsilon", type=float, default=1e-4)
    p.add_argument("--phases", type=float, nargs="+", default=[.125, .25, .5, .75, .875])
    p.add_argument("--max-nfev", type=int, default=60)
    p.add_argument("--check-jacobian", action="store_true",
                   help="Check the analytic metric Jacobian at the first nontrivial phase")
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    if args.epsilon <= 0:
        p.error("Use a fixed positive epsilon")
    prepared = second.prepare_profile_reference(args)
    model = grid_model(args, prepared, args.theta_n, args.xi_n)
    fields = model["fields"]
    columns = fields.shape[2]
    mass = np.einsum("n,nik,nil->kl", model["area"], fields, fields)
    chol = cholesky(mass, lower=True)
    exact_indices = np.zeros((columns, 2))
    exact_indices[-2, 0] = exact_indices[-1, 1] = 1
    white_span = chol.T @ exact_indices
    orthogonal, _ = qr(white_span, mode="full")
    C_perp = solve_triangular(chol.T, orthogonal[:, 2:], lower=False)
    initial = np.zeros(columns - 1)
    initial[0] = args.epsilon
    # A second grid never feeds the optimizer and uses identical physical coefficients.
    validation = grid_model(args, prepared, 2 * args.theta_n, max(96, args.xi_n + 32))
    phases = []
    jacobian_checked = False
    for fraction in args.phases:
        check_now = bool(args.check_jacobian and not jacobian_checked and abs(np.sin(np.pi * fraction)) > 1e-12)
        initial, coeff, record = slice_solve(args, model, C_perp, np.pi * fraction, initial, check_now)
        jacobian_checked = bool(jacobian_checked or check_now)
        Fs = validation["Xs"] + np.einsum("nik,k->ni", validation["fields_s"], coeff)
        Fu = validation["Xu"] + np.einsum("nik,k->ni", validation["fields_u"], coeff)
        metric = metric_error(validation, Fs, Fu)
        record["validation_max_relative_metric_frobenius"] = float(np.max(np.linalg.norm(metric, axis=1)))
        record["physical_coefficients"] = coeff.tolist()
        actual_E = np.sum(Fs * Fs, axis=1)
        actual_F = np.sum(Fs * Fu, axis=1)
        actual_G = np.sum(Fu * Fu, axis=1)
        record["validation_min_metric_determinant"] = float(np.min(actual_E * actual_G - actual_F * actual_F))
        if record["validation_max_relative_metric_frobenius"] < 1e-4:
            gaussian, principal = kernel.differential_geometry(validation["data"], Fs, Fu, validation["u"],
                                validation["xi_s"], validation["xi_u"], validation["y"], validation["yw"],
                                validation["xi_halfwidth"])
            record["validation_sampled_curvature"] = dict(gaussian_min=float(np.min(gaussian)),
                    gaussian_max=float(np.max(gaussian)), max_abs_principal=float(np.max(principal)))
        phases.append(record)
    result = dict(schema="literature-fixed-metric-newton-v1", source="https://arxiv.org/html/2611.17269v1",
                  status="Nonlinear path-slice experiment; a continuous isometric family has not been assumed",
                  parameters={k: val for k, val in vars(args).items() if k != "output"},
                  reference=prepared[2], profile_circle=prepared[6],
                  target_metric="One fixed g_epsilon=g_X+epsilon^2 dYf^2 at every phase and validation node",
                  boundary=("C2 zero-extension fields on the active strip; exp profile fields have all endpoint jets zero"
                            if args.profile_kind == "bump" else
                            "C2 zero-extension fields on the active strip; polynomial profiles have finite endpoint vanishing order"),
                  jacobian_check_performed=bool(jacobian_checked),
                  trial_columns=columns, mass_condition_number=float(np.linalg.cond(mass)),
                  validation_grid=dict(theta_n=2 * args.theta_n, xi_n=max(96, args.xi_n + 32)),
                  phase_slices=phases,
                  caveats=["Solver success is a stopping condition, not a metric-accuracy claim.",
                           "Finite phase samples do not yet establish an all-time family; coefficients require continuation and refinement.",
                           "Failure in this finite trial space is not a nonexistence result.",
                           "No closed surface, embedding, reach, or macroscopic grip displacement is claimed."])
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
