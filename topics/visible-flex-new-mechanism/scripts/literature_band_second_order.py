#!/usr/bin/env python3
"""Three-moment profile circle and complete second-order band compatibility.

Independent derivation: notes/literature-second-order-moments-20261114.md.
Public band source: https://arxiv.org/html/2611.17269v1, Section 2.
This tests two forcing channels, preserves every computed period defect, and
never calls a zero-mean projected correction an exact solution when defects remain.
Run research calculations in the public repository's GitHub Actions.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre as leg
from scipy.linalg import eigh

import literature_band_seed as seed
import literature_band_kernel as kernel


def theta_derivative(values):
    n = len(values)
    k = np.fft.fftfreq(n, 1 / n)
    return np.fft.ifft((1j * k).reshape((n,) + (1,) * (values.ndim - 1))
                      * np.fft.fft(values, axis=0), axis=0).real


def xi_operators(n, left, right):
    z, weights = leg.leggauss(n)
    halfwidth = (right - left) / 2
    xi = (left + right) / 2 + halfwidth * z
    V = leg.legvander(z, n)
    coefficients = ((2 * np.arange(n) + 1) / 2)[:, None] * V[:, :n].T * weights[None, :]
    right_integrals = np.zeros((n, n))
    right_integrals[:, 0] = 1 - z
    for j in range(1, n):
        right_integrals[:, j] = -(V[:, j + 1] - V[:, j - 1]) / (2 * j + 1)
    integrate_right = halfwidth * right_integrals @ coefficients
    bary = (-1.0)**np.arange(n) * np.sqrt((1 - z * z) * weights)
    difference = z[:, None] - z[None, :]
    np.fill_diagonal(difference, 1)
    D = bary[None, :] / bary[:, None] / difference
    np.fill_diagonal(D, 0)
    np.fill_diagonal(D, -np.sum(D, axis=1))
    D /= halfwidth
    endpoint = []
    for derivative_order in range(3):
        matrix = np.zeros((2, n))
        for j in range(n):
            coeff = np.zeros(j + 1)
            coeff[-1] = 1
            if j >= derivative_order:
                matrix[:, j] = leg.legval(np.array([-1., 1.]), leg.legder(coeff, derivative_order)) / halfwidth**derivative_order
        endpoint.append(matrix @ coefficients)
    return xi, halfwidth * weights, D, integrate_right, endpoint


def profile_circle(left, right, count):
    xi, weights, _, _, _ = xi_operators(512, left, right)
    profiles = [kernel.profile(xi, left, right, 2 * j) for j in range(count)]
    dp = np.column_stack([p[1] for p in profiles])
    ddp = np.column_stack([p[2] for p in profiles])
    A = ddp.T @ (weights[:, None] * ddp)
    B = ddp.T @ ((weights * xi * xi)[:, None] * ddp) + 2 * dp.T @ (weights[:, None] * dp)
    J1 = ddp.T @ ((weights * xi)[:, None] * ddp)
    eigenvalues, eigenvectors = eigh(B, A)
    mu = (eigenvalues[1] + eigenvalues[-2]) / 2
    if not eigenvalues[0] < mu < eigenvalues[-1] or not eigenvalues[1] < eigenvalues[-2]:
        raise ValueError("Need four separated generalized eigenvalues for this circle construction")
    f = (np.sqrt((eigenvalues[-1] - mu) / (eigenvalues[-1] - eigenvalues[0])) * eigenvectors[:, 0]
         + np.sqrt((mu - eigenvalues[0]) / (eigenvalues[-1] - eigenvalues[0])) * eigenvectors[:, -1])
    g = (np.sqrt((eigenvalues[-2] - mu) / (eigenvalues[-2] - eigenvalues[1])) * eigenvectors[:, 1]
         + np.sqrt((mu - eigenvalues[1]) / (eigenvalues[-2] - eigenvalues[1])) * eigenvectors[:, -2])
    def records(matrix):
        return dict(ff=float(f @ matrix @ f), gg=float(g @ matrix @ g), fg=float(f @ matrix @ g))
    diagnostics = dict(generalized_eigenvalues=eigenvalues.tolist(), common_rayleigh_value=float(mu),
                       even_profile_degrees=(2 * np.arange(count)).tolist(),
                       f_coefficients=f.tolist(), g_coefficients=g.tolist(),
                       moments_before_common_scaling=dict(J0=records(A), J1=records(J1), J2_star=records(B)),
                       A_condition_number=float(np.linalg.cond(A)))
    return f, g, diagnostics


def field_pair(data, v, vp, om, u, reference, f, g, scale):
    count = 2 * len(f) - 1
    fields = kernel.bending_fields(data, v, vp / data["sphere_speed"], om, u,
                                   reference["profile_left"], reference["profile_right"], count, scale)
    result = []
    for array in fields:
        even = array[:, :, ::2]
        result.append((np.einsum("nik,k->ni", even, f), np.einsum("nik,k->ni", even, g)))
    return result


def normalized_tensor(E, F, G, base_E):
    return np.sqrt((E / base_E)**2 + 2 * F * F / base_E + G * G)


def range_correction(H, geometry):
    """Solve by characteristics after projecting periods; retain all defects."""
    HE, HF, HG = H
    d, v, vp, u, xi, weights, D, integrate_right, endpoint, om = geometry
    nt, nx = u.shape
    sp = d["sphere_speed"][:, None]
    kappa = d["kappa"][:, None]
    ks = (d["kappa_theta"] / d["sphere_speed"])[:, None]
    vs = (vp / d["sphere_speed"])[:, None]
    h = np.sqrt(v)[:, None]
    xi_s = (vs / u - ks) / (2 * h)
    xi_u = -h / u**2
    w = v[:, None] - kappa * u
    E0 = w * w + u * u
    jacobian = h / (xi[None, :] + om[:, None])**2
    rho = .5 * (HG * jacobian) @ integrate_right.T
    ruling_defect = np.sum(weights[None, :] * HG * jacobian, axis=1)
    ruling_absolute = np.sum(weights[None, :] * np.abs(HG) * jacobian, axis=1)
    rho_xi = rho @ D.T
    rho_s = theta_derivative(rho) / sp + xi_s * rho_xi
    AA = HF - rho_s
    BB = HE / 2 + (w * kappa - u) * rho
    cc = u * (vs - ks * u) / (2 * v[:, None])
    SS = (BB + cc * AA) / u**2
    theta_rhs = sp * SS
    period = 2 * np.pi / nt * np.sum(theta_rhs, axis=0)
    period_absolute = 2 * np.pi / nt * np.sum(np.abs(theta_rhs), axis=0)
    W = seed.periodic_primitive(theta_rhs)
    W_xi = W @ D.T
    zeta = u * u * W
    zeta_u = 2 * u * W + u * u * xi_u * W_xi
    eta = (AA - zeta_u) / 2
    p = (zeta + u * eta) / v[:, None]
    q = eta - kappa * p
    Z = np.stack((p, rho, q), axis=-1)
    Z_xi = np.einsum("ij,ajk->aik", D, Z)
    components_s = theta_derivative(Z) / sp[:, :, None] + xi_s[:, :, None] * Z_xi
    Zs = components_s.copy()
    Zs[:, :, 0] -= kappa * rho
    Zs[:, :, 1] += kappa * p + q
    Zs[:, :, 2] -= rho
    Zu = xi_u[:, :, None] * Z_xi
    LE = 2 * (w * Zs[:, :, 0] - u * Zs[:, :, 2])
    LF = Zs[:, :, 1] + w * Zu[:, :, 0] - u * Zu[:, :, 2]
    LG = 2 * Zu[:, :, 1]
    target_size = float(np.max(normalized_tensor(HE, HF, HG, E0)))
    error = float(np.max(normalized_tensor(LE - HE, LF - HF, LG - HG, E0)))
    collar = []
    for order, op in enumerate(endpoint):
        jets = np.einsum("ij,ajk->aik", op, Z)
        collar.append(dict(xi_derivative_order=order, max_component_norm=float(np.max(np.linalg.norm(jets, axis=2)))))
    diagnostic = dict(ruling_integral_max_absolute=float(np.max(np.abs(ruling_defect))),
                      ruling_integral_relative=float(np.max(np.abs(ruling_defect))) / max(float(np.max(ruling_absolute)), 1e-300),
                      period_max_absolute=float(np.max(np.abs(period))),
                      period_relative_to_integrated_absolute=float(np.max(np.abs(period))) / max(float(np.max(period_absolute)), 1e-300),
                      period_samples=dict(xi=xi.tolist(), period=period.tolist()),
                      forcing_max_gX_relative_frobenius=target_size,
                      projected_correction_full_equation_max_gX_relative_frobenius=error,
                      projected_correction_full_equation_relative_to_forcing=error / max(target_size, 1e-300),
                      projected_correction_max_norm=float(np.max(np.linalg.norm(Z, axis=2))),
                      projected_correction_collar_jets=collar,
                      correction_status="Diagnostic zero-period projection; it is a solution only if displayed original defects converge to zero")
    return (Z, Zs, Zu), diagnostic


def fast_period_operator(data, v, vp, om, u, xi):
    """Six preintegrated coefficients for the quadratic Volterra obstruction."""
    sp = data["sphere_speed"][:, None]
    kappa = data["kappa"][:, None]
    ks = (data["kappa_theta"] / data["sphere_speed"])[:, None]
    h = np.sqrt(v)[:, None]
    hs = (vp / data["sphere_speed"])[:, None] / (2 * h)
    oms = ks / (2 * h)
    z = xi[None, :] + om[:, None]
    cstar = hs / z - h * oms / z**2
    Vt = oms / (2 * z**2)
    Vn = -h / 2 + np.zeros_like(u)
    Vb = -hs / 2 + ks / (2 * z) - kappa * oms / (2 * z**2)
    local_a = (u * u + cstar * cstar) / (2 * u * u)
    local_b = (u * Vn + cstar * Vb) / (u * u)
    local_c = (Vt * Vt + Vn * Vn + Vb * Vb) / (2 * u * u)
    inverse_u_ss = theta_derivative(theta_derivative(1 / u) / sp) / sp
    K = kappa * z * z - (kappa * kappa + 1) * z / h - inverse_u_ss
    rlocal = [u / 2, -h / 2 + kappa / (2 * z),
              h * z / 4 - 3 * kappa / 8 + (kappa * kappa + 1) / (8 * h * z)]
    rtail = [((h * om[:, None] - kappa)**2 + 1) / (8 * h),
             (h * om[:, None] - kappa) / 4, h / 8]
    integrate = lambda value: 2 * np.pi / len(data["theta"]) * np.sum(sp * value, axis=0)
    return [integrate(local + K * rr) for local, rr in zip([local_a, local_b, local_c], rlocal)] + [integrate(K * rr) for rr in rtail]


def profile_values(xi, left, right, coeff, scale):
    basis = [kernel.profile(xi, left, right, 2 * j) for j in range(len(coeff))]
    return tuple(scale * sum(coeff[j] * basis[j][order] for j in range(len(coeff))) for order in range(3))


def quadratic_period(coefficients, first, second, xi, integrate_right):
    f, fp, fpp = first
    g, gp, gpp = second
    J0 = integrate_right @ (fpp * gpp)
    J1 = integrate_right @ (xi * fpp * gpp)
    J2 = integrate_right @ (xi * xi * fpp * gpp + 2 * fp * gp)
    a, b, c, d0, d1, d2 = coefficients
    return a * f * g + b * (f * gp + fp * g) / 2 + c * fp * gp + d0 * J0 + d1 * J1 + d2 * J2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=3)
    parser.add_argument("--power", type=float, default=1)
    parser.add_argument("--center", type=float, default=-3)
    parser.add_argument("--sigma", type=float, default=1.5)
    parser.add_argument("--delta", type=float, default=.3)
    parser.add_argument("--theta-n", type=int, default=384)
    parser.add_argument("--xi-n", type=int, default=64)
    parser.add_argument("--profile-count", type=int, default=4)
    parser.add_argument("--epsilon", type=float, nargs="+", default=[1e-5, 1e-4, 1e-3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.profile_count < 4:
        parser.error("Use at least four even profiles")
    parameters, amplitude, reference = kernel.build_reference(args)
    f, g, moment_data = profile_circle(reference["profile_left"], reference["profile_right"], args.profile_count)
    # Freeze the common field normalization on a reference grid, not the tested grid.
    rd = seed.spherical_data(args.q, parameters.a, "curvature", .85, 2048)
    rv, rvp = seed.speed_data(parameters, rd, amplitude)
    rom = kernel.omega(rd["kappa"], parameters, amplitude)
    rxi, _, _, _, _ = xi_operators(128, reference["profile_left"], reference["profile_right"])
    ru = np.sqrt(rv)[:, None] / (rxi[None, :] + rom[:, None])
    raw = field_pair(rd, rv, rvp, rom, ru, reference, f, g, 1)
    maximum = max(float(np.max(np.linalg.norm(raw[0][0], axis=1))), float(np.max(np.linalg.norm(raw[0][1], axis=1))))
    common_scale = reference["sampled_reference_diameter"] / maximum
    del raw
    moment_data["common_field_scale"] = common_scale
    d = seed.spherical_data(args.q, parameters.a, "curvature", .85, args.theta_n)
    v, vp = seed.speed_data(parameters, d, amplitude)
    om = kernel.omega(d["kappa"], parameters, amplitude)
    xi, weights, D, integrate_right, endpoint = xi_operators(args.xi_n, reference["profile_left"], reference["profile_right"])
    u = np.sqrt(v)[:, None] / (xi[None, :] + om[:, None])
    pair = field_pair(d, v, vp, om, u, reference, f, g, common_scale)
    (Yf, Yg), (Yfs, Ygs), (Yfu, Ygu) = [(x.reshape(args.theta_n, args.xi_n, 3), y.reshape(args.theta_n, args.xi_n, 3)) for x, y in pair]
    dot = lambda x, y: np.sum(x * y, axis=2)
    Hd = (dot(Yfs, Yfs) - dot(Ygs, Ygs), dot(Yfs, Yfu) - dot(Ygs, Ygu), dot(Yfu, Yfu) - dot(Ygu, Ygu))
    Hc = (-2 * dot(Yfs, Ygs), -dot(Yfs, Ygu) - dot(Ygs, Yfu), -2 * dot(Yfu, Ygu))
    geometry = (d, v, vp, u, xi, weights, D, integrate_right, endpoint, om)
    Zd, diag_d = range_correction(Hd, geometry)
    Zc, diag_c = range_correction(Hc, geometry)
    fast_coefficients = fast_period_operator(d, v, vp, om, u, xi)
    f_values = profile_values(xi, reference["profile_left"], reference["profile_right"], f, common_scale)
    g_values = profile_values(xi, reference["profile_left"], reference["profile_right"], g, common_scale)
    fast_diagonal = (quadratic_period(fast_coefficients, f_values, f_values, xi, integrate_right)
                     - quadratic_period(fast_coefficients, g_values, g_values, xi, integrate_right))
    fast_cross = -2 * quadratic_period(fast_coefficients, f_values, g_values, xi, integrate_right)
    fast = dict(coefficient_names=["phi_squared", "phi_phi_prime", "phi_prime_squared", "tail_J0", "tail_J1", "tail_J2_star"],
                coefficients=[a.tolist() for a in fast_coefficients],
                diagonal_period=fast_diagonal.tolist(), cross_period=fast_cross.tolist(),
                diagonal_vs_direct_max_absolute=float(np.max(np.abs(fast_diagonal - np.array(diag_d["period_samples"]["period"])))),
                cross_vs_direct_max_absolute=float(np.max(np.abs(fast_cross - np.array(diag_c["period_samples"]["period"])))))
    w = v[:, None] - d["kappa"][:, None] * u
    Xs = np.stack((w, np.zeros_like(w), -u), axis=-1)
    Xu = np.zeros_like(Xs)
    Xu[:, :, 1] = 1
    paths = []
    for eps in args.epsilon:
        Es = Xs + eps * Yfs
        Eu = Xu + eps * Yfu
        E, F, G = dot(Es, Es), dot(Es, Eu), dot(Eu, Eu)
        determinant = E * G - F * F
        rows = []
        for fraction in [0, .125, .25, .375, .5, .75, 1]:
            t = np.pi * fraction
            ct, st = np.cos(t), np.sin(t)
            Zs = st * st * Zd[1] + st * ct * Zc[1]
            Zu = st * st * Zd[2] + st * ct * Zc[2]
            Fs = Xs + eps * (ct * Yfs + st * Ygs) + eps**2 * Zs
            Fu = Xu + eps * (ct * Yfu + st * Ygu) + eps**2 * Zu
            dE, dF, dG = dot(Fs, Fs) - E, dot(Fs, Fu) - F, dot(Fu, Fu) - G
            orth1 = dE / E
            orth2 = np.sqrt(2) * (E * dF - F * dE) / (E * np.sqrt(determinant))
            orth3 = (F * F * dE - 2 * E * F * dF + E * E * dG) / (E * determinant)
            error = float(np.max(np.sqrt(orth1**2 + orth2**2 + orth3**2)))
            rows.append(dict(t_over_pi=fraction, max_relative_metric_frobenius_error=error))
        paths.append(dict(epsilon=eps, samples=rows,
                          maximum_sampled_metric_error=max(x["max_relative_metric_frobenius_error"] for x in rows)))
    result = dict(schema="literature-second-order-v1", source="https://arxiv.org/html/2611.17269v1",
                  status="Second-order compatibility experiment; no finite isometric family asserted",
                  parameters={k: val for k, val in vars(args).items() if k != "output"},
                  reference=reference, profile_circle=moment_data,
                  channels=dict(diagonal=diag_d, cross=diag_c), fast_volterra_operator=fast,
                  fixed_epsilon_truncated_path_checks=paths,
                  caveats=["The three moments solve only the ruling condition; period functions must also vanish.",
                           "Zero-mean projection retains and reports the original obstruction, not an exact correction.",
                           "Changing epsilon changes the target metric and is not fixed-metric refinement.",
                           "Profiles differ from the previous single-bump kernel input; this is a new design.",
                           "No closed surface, embedding, reach, or requested amplitude is claimed."])
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
