#!/usr/bin/env python3
"""Galerkin diagnostic for fixed-boundary infinitesimal bendings at F+=X+epsY.

Public-source input: arXiv:2611.17269v1, Section 2.  The fixed metric at each
separate epsilon is g_epsilon, not g_X.  This diagnoses a finite trial space;
positive singular values do NOT prove infinitesimal or finite rigidity.
Research jobs belong in this repository's GitHub Actions.
"""
import argparse
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from numpy.polynomial import legendre as leg
from scipy.linalg import cholesky, solve_triangular, svdvals

import literature_band_seed as seed


def curvature_speed(kappa, parameters, amplitude):
    base = (1 + kappa * kappa)**(parameters.power / 2)
    window = np.exp(-0.5 * ((kappa - parameters.center) / parameters.sigma)**2)
    return base * (1 + amplitude * window)


def omega(kappa, parameters, amplitude, order=192):
    """omega(k)=1/2 integral_0^k 1/sqrt(V(x)) dx, evaluated by Gauss quadrature."""
    nodes, weights = leg.leggauss(order)
    points = kappa[:, None] * (nodes[None, :] + 1) / 2
    return kappa * np.sum(weights[None, :] / np.sqrt(curvature_speed(points, parameters, amplitude)), axis=1) / 4


def profile(xi, left, right, degree):
    z = (2 * xi - left - right) / (right - left)
    halfwidth = (right - left) / 2
    p = np.zeros_like(z)
    dp = np.zeros_like(z)
    ddp = np.zeros_like(z)
    mask = np.abs(z) < 1
    zm = z[mask]
    d = 1 - zm * zm
    bump = np.exp(1 - 1 / d)
    logp = -2 * zm / d**2
    logpp = -2 / d**2 - 8 * zm * zm / d**3
    coeff = np.zeros(degree + 1)
    coeff[-1] = 1
    polynomial = leg.legval(zm, coeff)
    polynomial_p = leg.legval(zm, leg.legder(coeff)) if degree else np.zeros_like(zm)
    polynomial_pp = leg.legval(zm, leg.legder(coeff, 2)) if degree > 1 else np.zeros_like(zm)
    p[mask] = bump * polynomial
    dp[mask] = bump * (logp * polynomial + polynomial_p) / halfwidth
    ddp[mask] = bump * ((logp * logp + logpp) * polynomial + 2 * logp * polynomial_p + polynomial_pp) / halfwidth**2
    return p, dp, ddp


def bending_fields(data, v, vs, om, u, left, right, count, scale=1):
    """Return components in (T,N,B), plus true s/u derivatives in that frame."""
    kappa = data["kappa"][:, None]
    ks = (data["kappa_theta"] / data["sphere_speed"])[:, None]
    v, vs, om = v[:, None], vs[:, None], om[:, None]
    u = np.asarray(u)
    if u.ndim == 1:
        u = u[None, :]
    h = np.sqrt(v)
    w = v - kappa * u
    xi = h / u - om
    xis = (vs / u - ks) / (2 * h)
    values, ds, du = [], [], []
    for degree in range(count):
        phi, phip, phipp = profile(xi, left, right, degree)
        P = -u * phip / (2 * h)
        Q = u * phi - w * phip / (2 * h)
        Ps = u * vs * phip / (4 * h**3) - u * phipp * xis / (2 * h)
        Qs = u * phip * xis - ((vs - ks * u) / (2 * h) - w * vs / (4 * h**3)) * phip - w * phipp * xis / (2 * h)
        Pu = -phip / (2 * h) + phipp / (2 * u)
        Qu = phi - h * phip / u + kappa * phip / (2 * h) + w * phipp / (2 * u**2)
        zero = np.zeros_like(P)
        values.append(scale * np.stack((P, zero, Q), axis=-1).reshape(-1, 3))
        ds.append(scale * np.stack((Ps, kappa * P + Q, Qs), axis=-1).reshape(-1, 3))
        du.append(scale * np.stack((Pu, zero, Qu), axis=-1).reshape(-1, 3))
    return np.stack(values, axis=-1), np.stack(ds, axis=-1), np.stack(du, axis=-1)


def build_reference(args):
    parameters = SimpleNamespace(kind="curvature", q=args.q, a=1 / args.q, b=.85,
                                 power=args.power, center=args.center, sigma=args.sigma,
                                 reference_n=32768)
    amplitude, integrals = seed.closing_amplitude(parameters)
    d = seed.spherical_data(args.q, parameters.a, "curvature", .85, 2048)
    v, vp = seed.speed_data(parameters, d, amplitude)
    alpha = seed.periodic_primitive(v[:, None] * d["raw"])
    diameter = seed.sampled_diameter(alpha)
    om = omega(d["kappa"], parameters, amplitude)
    left = 1.1 * float(np.max(np.sqrt(v) / args.delta - om))
    right = left + max(left, 1)
    z, _ = leg.leggauss(128)
    xi = (left + right) / 2 + (right - left) / 2 * z
    u = np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])
    Y, _, _ = bending_fields(d, v, vp / d["sphere_speed"], om, u, left, right, 1)
    raw_max = float(np.max(np.linalg.norm(Y[:, :, 0], axis=1)))
    scale = diameter / raw_max
    omega_error = float(np.max(np.abs(om - omega(d["kappa"], parameters, amplitude, order=384))))
    return parameters, amplitude, dict(reference_integrals=integrals, amplitude=amplitude,
                                      sampled_reference_diameter=diameter, profile_left=left,
                                      profile_right=right, field_scale=scale,
                                      raw_field_sampled_max=raw_max,
                                      omega_quadrature_192_vs_384_error=omega_error)


def basis(data, y, xi_halfwidth, modes, degree, xi_s, xi_u):
    theta = data["theta"]
    angular = [np.ones_like(theta)]
    angular_p = [np.zeros_like(theta)]
    for m in range(1, modes + 1):
        angular.extend([np.sqrt(2) * np.cos(m * theta), np.sqrt(2) * np.sin(m * theta)])
        angular_p.extend([-m * np.sqrt(2) * np.sin(m * theta), m * np.sqrt(2) * np.cos(m * theta)])
    angular = np.stack(angular, axis=1)
    angular_p = np.stack(angular_p, axis=1) / data["sphere_speed"][:, None]
    envelope = (1 - y * y)**3
    envelope_p = -6 * y * (1 - y * y)**2
    polynomials = leg.legvander(y, degree)
    polynomial_p = np.zeros_like(polynomials)
    for j in range(1, degree + 1):
        coeff = np.zeros(j + 1)
        coeff[-1] = 1
        polynomial_p[:, j] = leg.legval(y, leg.legder(coeff))
    radial = envelope[:, None] * polynomials
    radial_p = (envelope_p[:, None] * polynomials + envelope[:, None] * polynomial_p) / xi_halfwidth
    def product(a, b):
        return np.einsum("am,bn->abmn", a, b).reshape(len(theta) * len(y), -1)
    value = product(angular, radial)
    derivative_xi = product(angular, radial_p)
    derivative_s = product(angular_p, radial) + xi_s.ravel()[:, None] * derivative_xi
    derivative_u = xi_u.ravel()[:, None] * derivative_xi
    return value, derivative_s, derivative_u


def differential_geometry(data, Fs, Fu, u, xi_s, xi_u, y, yw, xi_halfwidth):
    """Nodal second fundamental form; refinement diagnostics, not certificates."""
    nt, ny = u.shape
    Fs, Fu = Fs.reshape(nt, ny, 3), Fu.reshape(nt, ny, 3)
    speed = data["sphere_speed"][:, None]
    kappa = data["kappa"][:, None]
    u_theta = -speed * xi_s / xi_u
    Ft = speed[:, :, None] * Fs + u_theta[:, :, None] * Fu
    Fx = Fu / xi_u[:, :, None]
    k = np.fft.fftfreq(nt, 1 / nt)
    Ft_theta = np.fft.ifft(1j * k[:, None, None] * np.fft.fft(Ft, axis=0), axis=0).real
    Ft_theta[:, :, 0] -= speed * kappa * Ft[:, :, 1]
    Ft_theta[:, :, 1] += speed * (kappa * Ft[:, :, 0] + Ft[:, :, 2])
    Ft_theta[:, :, 2] -= speed * Ft[:, :, 1]
    bary = (-1.0)**np.arange(ny) * np.sqrt((1 - y * y) * yw)
    difference = y[:, None] - y[None, :]
    np.fill_diagonal(difference, 1)
    derivative = bary[None, :] / bary[:, None] / difference
    np.fill_diagonal(derivative, 0)
    np.fill_diagonal(derivative, -np.sum(derivative, axis=1))
    derivative /= xi_halfwidth
    Ft_xi = np.einsum("ij,ajk->aik", derivative, Ft)
    Fx_xi = np.einsum("ij,ajk->aik", derivative, Fx)
    normal = np.cross(Fs, Fu)
    normal /= np.linalg.norm(normal, axis=2)[:, :, None]
    L = np.sum(normal * Ft_theta, axis=2)
    M = np.sum(normal * Ft_xi, axis=2)
    NN = np.sum(normal * Fx_xi, axis=2)
    EE = np.sum(Ft * Ft, axis=2)
    FF = np.sum(Ft * Fx, axis=2)
    GG = np.sum(Fx * Fx, axis=2)
    determinant = EE * GG - FF * FF
    gaussian = (L * NN - M * M) / determinant
    trace = (EE * NN - 2 * FF * M + GG * L) / determinant
    discriminant = np.maximum(trace * trace - 4 * gaussian, 0)
    principal_abs = (np.abs(trace) + np.sqrt(discriminant)) / 2
    return gaussian, principal_abs


def evaluate(args, parameters, amplitude, reference, epsilon):
    d = seed.spherical_data(args.q, parameters.a, "curvature", .85, args.theta_n)
    v, vp = seed.speed_data(parameters, d, amplitude)
    om = omega(d["kappa"], parameters, amplitude)
    y, yw = leg.leggauss(args.u_n)
    xi_halfwidth = (reference["profile_right"] - reference["profile_left"]) / 2
    xi = (reference["profile_right"] + reference["profile_left"]) / 2 + xi_halfwidth * y
    u = np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])
    xi_s = ((vp / d["sphere_speed"])[:, None] / u
            - (d["kappa_theta"] / d["sphere_speed"])[:, None]) / (2 * np.sqrt(v)[:, None])
    xi_u = -np.sqrt(v)[:, None] / u**2
    Y, Ys, Yu = bending_fields(d, v, vp / d["sphere_speed"], om, u,
                               reference["profile_left"], reference["profile_right"],
                               args.exact_fields, reference["field_scale"])
    kappa = np.repeat(d["kappa"], args.u_n)
    w = (v[:, None] - d["kappa"][:, None] * u).ravel()
    U = u.ravel()
    Xs = np.column_stack((w, np.zeros_like(w), -U))
    Xu = np.column_stack((np.zeros_like(w), np.ones_like(w), np.zeros_like(w)))
    Fs = Xs + epsilon * Ys[:, :, 0]
    Fu = Xu + epsilon * Yu[:, :, 0]
    E = np.sum(Fs * Fs, axis=1)
    F = np.sum(Fs * Fu, axis=1)
    G = np.sum(Fu * Fu, axis=1)
    det = E * G - F * F
    u_jacobian = xi_halfwidth * np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])**2
    area_weights = (2 * np.pi / args.theta_n * u_jacobian.ravel()
                    * np.repeat(d["sphere_speed"], args.u_n) * np.tile(yw, args.theta_n) * np.sqrt(det))
    psi, ps, pu = basis(d, y, xi_halfwidth, args.modes, args.degree, xi_s, xi_u)
    K = psi.shape[1]
    A, C, B = Fs.T
    a, c, b = Fu.T
    multiply = lambda z, mat: z[:, None] * mat
    dE = 2 * np.concatenate((multiply(A, ps) + multiply(C * kappa, psi),
                              multiply(-A * kappa - B, psi) + multiply(C, ps),
                              multiply(C, psi) + multiply(B, ps)), axis=1)
    dF = np.concatenate((multiply(a, ps) + multiply(c * kappa, psi) + multiply(A, pu),
                         multiply(-a * kappa - b, psi) + multiply(c, ps) + multiply(C, pu),
                         multiply(c, psi) + multiply(b, ps) + multiply(B, pu)), axis=1)
    dG = 2 * np.concatenate((multiply(a, pu), multiply(c, pu), multiply(b, pu)), axis=1)
    exact_dE = 2 * np.einsum("ni,nik->nk", Fs, Ys)
    exact_dF = np.einsum("ni,nik->nk", Fs, Yu) + np.einsum("ni,nik->nk", Fu, Ys)
    exact_dG = 2 * np.einsum("ni,nik->nk", Fu, Yu)
    dE, dF, dG = [np.concatenate((regular, exact), axis=1)
                   for regular, exact in [(dE, exact_dE), (dF, exact_dF), (dG, exact_dG)]]
    normalized = [dE / E[:, None],
                  np.sqrt(2) * (E[:, None] * dF - F[:, None] * dE) / (E * np.sqrt(det))[:, None],
                  (F[:, None]**2 * dE - 2 * (E * F)[:, None] * dF + E[:, None]**2 * dG) / (E * det)[:, None]]
    operator = np.concatenate([np.sqrt(area_weights)[:, None] * mat for mat in normalized], axis=0)
    mass_scalar = psi.T @ (area_weights[:, None] * psi)
    columns = 3 * K + args.exact_fields
    mass = np.zeros((columns, columns))
    for j in range(3):
        sl = slice(j * K, (j + 1) * K)
        mass[sl, sl] = mass_scalar
        cross = psi.T @ (area_weights[:, None] * Y[:, j, :])
        mass[sl, 3 * K:] = cross
        mass[3 * K:, sl] = cross.T
    mass[3 * K:, 3 * K:] = np.einsum("n,nik,nil->kl", area_weights, Y, Y)
    chol = cholesky(mass, lower=True)
    whitened = solve_triangular(chol, operator.T, lower=True).T
    singular = svdvals(whitened)
    baseline_residual = max(float(np.max(np.abs(2 * np.einsum("ni,nik->nk", Xs, Ys)))),
                            float(np.max(np.abs(np.einsum("ni,nik->nk", Xs, Yu) + np.einsum("ni,nik->nk", Xu, Ys)))),
                            float(np.max(np.abs(2 * np.einsum("ni,nik->nk", Xu, Yu)))))
    diameter = reference["sampled_reference_diameter"]
    E0 = w * w + U * U
    hs = np.sum(Ys[:, :, 0]**2, axis=1)
    hu = np.sum(Yu[:, :, 0]**2, axis=1)
    hsu = np.sum(Ys[:, :, 0] * Yu[:, :, 0], axis=1)
    aa, cc, bb = epsilon**2 * hs / E0, epsilon**2 * hu, epsilon**2 * hsu / np.sqrt(E0)
    metric_perturbation = (aa + cc + np.sqrt((aa - cc)**2 + 4 * bb * bb)) / 2
    Fms, Fmu = Xs - epsilon * Ys[:, :, 0], Xu - epsilon * Yu[:, :, 0]
    endpoint_metric_difference = max(float(np.max(np.abs(E - np.sum(Fms * Fms, axis=1)) / E)),
                                    float(np.max(np.abs(F - np.sum(Fms * Fmu, axis=1)) / np.sqrt(E * G))),
                                    float(np.max(np.abs(G - np.sum(Fmu * Fmu, axis=1)) / G)))
    gaussian, principal_abs = differential_geometry(d, Fs, Fu, u, xi_s, xi_u, y, yw, xi_halfwidth)
    geometry = dict(sampled_gaussian_curvature_min=float(np.min(gaussian)),
                    sampled_gaussian_curvature_max=float(np.max(gaussian)),
                    sampled_max_abs_principal_curvature=float(np.max(principal_abs)),
                    sampled_principal_radius_over_reference_D=1 / (diameter * float(np.max(principal_abs))))
    if epsilon == 0:
        exact_gaussian = -(np.repeat(v, args.u_n)**2 / E0**2).reshape(u.shape)
        geometry["X_gaussian_relative_nodal_error"] = float(np.max(np.abs(gaussian - exact_gaussian)
                                                                 / np.maximum(np.abs(exact_gaussian), 1 / diameter**2)))
    return dict(epsilon=epsilon, rows=operator.shape[0], columns=columns,
                smallest_dimensionless_singular_values=(diameter * singular[-min(12, columns):][::-1]).tolist(),
                largest_dimensionless_singular_value=float(diameter * singular[0]),
                min_metric_determinant=float(np.min(det)),
                known_X_bending_identity_max_absolute_residual=baseline_residual,
                sampled_field_max_over_reference_D=float(np.max(np.linalg.norm(Y[:, :, 0], axis=1))) / diameter,
                mass_condition_number=float(np.linalg.cond(mass)),
                max_relative_metric_perturbation_from_X=float(np.max(metric_perturbation)),
                endpoint_plus_minus_relative_metric_error=endpoint_metric_difference,
                differential_geometry=geometry)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--q", type=int, default=3)
    p.add_argument("--power", type=float, default=1)
    p.add_argument("--center", type=float, default=-3)
    p.add_argument("--sigma", type=float, default=1.5)
    p.add_argument("--delta", type=float, default=.3)
    p.add_argument("--theta-n", type=int, default=96)
    p.add_argument("--u-n", type=int, default=40)
    p.add_argument("--modes", type=int, default=6)
    p.add_argument("--degree", type=int, default=10)
    p.add_argument("--exact-fields", type=int, default=4)
    p.add_argument("--epsilon", type=float, nargs="+", default=[0, .005, .01])
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    if args.exact_fields < 1 or args.delta <= 0:
        p.error("Use positive delta and at least one exact bending field")
    parameters, amplitude, reference = build_reference(args)
    result = dict(schema="literature-band-kernel-v1", source="https://arxiv.org/html/2611.17269v1",
                  status="Finite-trial-space linearized diagnostic; no rigidity or flexibility theorem",
                  parameters={k: v for k, v in vars(args).items() if k != "output"},
                  reference=reference,
                  basis="Fourier(theta) times (1-z^2)^3 Legendre(z), z affine in xi, in (T,N,B), plus exact compact bending fields of X",
                  boundary="Value and first two derivatives vanish at both boundaries of the SAME characteristic strip as Y0",
                  support="Trial fields vanish outside Y0 active strip; unchanged disjoint-support kernel fields are excluded",
                  metric="Each epsilon labels a separate fixed g_epsilon; varying epsilon itself is not an isometric family",
                  spectra=[evaluate(args, parameters, amplitude, reference, e) for e in args.epsilon],
                  caveats=["Tiny Galerkin singular values need resolution convergence and nonlinear continuation.",
                           "Positive finite-dimensional singular values do not exclude omitted smooth kernel fields.",
                           "The exact X bending fields supply a zero-mode baseline at epsilon=0.",
                           "No embedding, reach, cap, or global closed-surface claim is made."])
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
