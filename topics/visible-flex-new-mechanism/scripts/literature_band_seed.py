#!/usr/bin/env python3
"""Closed-curve seeds for the band in arXiv:2611.17269v1, Section 2.

The curvature-speed and symmetric variants are independent derivations in
notes/literature-20261114.md.  This generates a ruled BAND and period diagnostics,
not a finite isometric flex, a closed surface, or a reach certificate.

Run research/refinement jobs in this public repository's GitHub Actions.
The amplitude is fixed using reference quadrature, then held fixed at every
reported resolution.  Its exact mathematical definition is a ratio of integrals.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist


def periodic_primitive(values):
    """Fourier primitive; report the removed zero mode separately as closure."""
    n = len(values)
    k = np.fft.fftfreq(n, 1 / n)
    multiplier = np.zeros(n, dtype=complex)
    multiplier[k != 0] = 1 / (1j * k[k != 0])
    return np.fft.ifft(multiplier[:, None] * np.fft.fft(values, axis=0), axis=0).real


def spherical_data(q, a, kind, b, n):
    """Analytic theta derivatives; no differentiation of sampled curvature."""
    theta = np.arange(n) * (2 * np.pi / n)
    x = q * theta
    if kind == "curvature":
        r = 1 + a * np.sin(x)
        rp = a * q * np.cos(x)
        rpp = -a * q**2 * np.sin(x)
        rppp = -a * q**3 * np.cos(x)
        phi = theta + 2 * np.sin(x) / q
        fp = 1 + 2 * np.cos(x)
        fpp = -2 * q * np.sin(x)
        fppp = -2 * q**2 * np.cos(x)
    else:
        r = 1 + a * np.cos(x)
        rp = -a * q * np.sin(x)
        rpp = -a * q**2 * np.cos(x)
        rppp = a * q**3 * np.sin(x)
        phi = theta + b * np.sin(2 * x) / q
        fp = 1 + 2 * b * np.cos(2 * x)
        fpp = -4 * b * q * np.sin(2 * x)
        fppp = -8 * b * q**2 * np.cos(2 * x)
    S = 1 + r * r
    f = np.column_stack((r * np.cos(phi), r * np.sin(phi), np.ones(n)))
    df = np.column_stack((rp * np.cos(phi) - r * fp * np.sin(phi),
                          rp * np.sin(phi) + r * fp * np.cos(phi), np.zeros(n)))
    B = f / np.sqrt(S)[:, None]
    B_theta = df / np.sqrt(S)[:, None] - f * (r * rp / S**1.5)[:, None]
    Q = rp * rp + r * r * S * fp * fp
    Qp = 2 * rp * rpp + 2 * r * rp * (1 + 2 * r * r) * fp * fp + 2 * r * r * S * fp * fpp
    J = 2 * rp * rp * fp + r * rp * fpp - r * rpp * fp + r * r * fp**3
    Jp = (3 * rp * rpp * fp + 3 * rp * rp * fpp + r * rp * fppp
          - r * rppp * fp + 2 * r * rp * fp**3 + 3 * r * r * fp * fp * fpp)
    speed = np.sqrt(Q) / S
    curvature = J * S**1.5 / Q**1.5
    curvature_theta = (Jp + J * (3 * r * rp / S - 1.5 * Qp / Q)) * S**1.5 / Q**1.5
    return dict(theta=theta, r=r, rp=rp, B=B, B_theta=B_theta, sphere_speed=speed,
                kappa=curvature, kappa_theta=curvature_theta,
                raw=-np.cross(B, B_theta))


def closing_amplitude(args):
    data = spherical_data(args.q, args.a, args.kind, args.b, args.reference_n)
    if args.kind == "symmetric":
        return None, None
    kappa = data["kappa"]
    base = (1 + kappa * kappa)**(args.power / 2)
    window = np.exp(-0.5 * ((kappa - args.center) / args.sigma)**2)
    factor = 2 * np.pi / args.reference_n
    I0 = float(factor * np.sum(base * data["raw"][:, 2]))
    I1 = float(factor * np.sum(base * window * data["raw"][:, 2]))
    if not I0 < 0 < I1:
        raise ValueError(f"Positive closing amplitude unavailable: I0={I0}, I1={I1}")
    return -I0 / I1, dict(I0=I0, I1=I1, reference_n=args.reference_n)


def speed_data(args, data, amplitude):
    kappa, kp = data["kappa"], data["kappa_theta"]
    if args.kind == "curvature":
        base = (1 + kappa * kappa)**(args.power / 2)
        window = np.exp(-0.5 * ((kappa - args.center) / args.sigma)**2)
        v = base * (1 + amplitude * window)
        vp = base * kp * (args.power * kappa / (1 + kappa * kappa) * (1 + amplitude * window)
                         - amplitude * window * (kappa - args.center) / args.sigma**2)
        return v, vp
    x = args.q * data["theta"]
    eta = 2 * args.b * args.c - 1 - args.c**2 / 2
    lam = ((1 - args.c * np.cos(2 * x))**2 + eta) / (2 * args.b * args.c)
    lamp = 2 * args.q / args.b * (1 - args.c * np.cos(2 * x)) * np.sin(2 * x)
    factor = 1 + 1 / data["r"]**2
    v = factor * lam
    vp = -2 * data["rp"] / data["r"]**3 * lam + factor * lamp
    return v, vp


def sampled_diameter(points):
    hull = ConvexHull(points)
    return float(np.max(pdist(points[hull.vertices])))


def evaluate(args, n, amplitude):
    data = spherical_data(args.q, args.a, args.kind, args.b, n)
    v, v_theta = speed_data(args, data, amplitude)
    d_alpha = v[:, None] * data["raw"]
    factor = 2 * np.pi / n
    closure = factor * np.sum(d_alpha, axis=0)
    period = float(factor * np.sum(data["kappa_theta"] / np.sqrt(v)))
    alpha = periodic_primitive(d_alpha)
    # The diameter uses at most 2048 samples.  It is a diagnostic lower estimate.
    index = np.arange(0, n, max(1, n // 2048))
    D = sampled_diameter(alpha[index])
    delta = args.fixed_halfwidth
    N = data["B_theta"] / data["sphere_speed"][:, None]
    band_ends = np.concatenate((alpha[index] - delta * N[index], alpha[index] + delta * N[index]))
    D_band = sampled_diameter(band_ends)
    max_curvature = 0.0
    min_w = float("inf")
    kappa_s = data["kappa_theta"] / data["sphere_speed"]
    v_s = v_theta / data["sphere_speed"]
    for u in np.linspace(-delta, delta, args.width_samples):
        w = v - data["kappa"] * u
        E = w * w + u * u
        h = u * (v_s - kappa_s * u) / E**1.5
        abs_principal = (np.abs(h) + np.sqrt(h * h + 4 * (v / E)**2)) / 2
        max_curvature = max(max_curvature, float(np.max(abs_principal)))
        min_w = min(min_w, float(np.min(w)))
    return dict(n=n, closure_vector=closure.tolist(), closure_norm=float(np.linalg.norm(closure)),
                closure_over_sampled_centerline_diameter=float(np.linalg.norm(closure)) / D,
                asymptotic_period=period, min_speed=float(np.min(v)),
                min_sphere_parameter_speed=float(np.min(data["sphere_speed"])),
                sampled_centerline_diameter=D, sampled_band_diameter=D_band,
                halfwidth=delta, halfwidth_over_sampled_band_diameter=delta / D_band,
                min_sampled_w=min_w, sampled_max_abs_principal_curvature=max_curvature,
                sampled_principal_radius_over_centerline_diameter=1 / (max_curvature * D),
                sampled_principal_radius_over_band_diameter=1 / (max_curvature * D_band))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["curvature", "symmetric"], default="curvature")
    parser.add_argument("--q", type=int, default=3)
    parser.add_argument("--a", type=float)
    parser.add_argument("--b", type=float, default=0.85)
    parser.add_argument("--c", type=float, default=1.7)
    parser.add_argument("--power", type=float, default=1.0)
    parser.add_argument("--center", type=float, default=-3.0)
    parser.add_argument("--sigma", type=float, default=1.5)
    parser.add_argument("--reference-n", type=int, default=32768)
    parser.add_argument("--n", type=int, nargs="+", default=[512, 1024, 2048, 4096, 8192])
    parser.add_argument("--width", type=float, default=0.03)
    parser.add_argument("--width-samples", type=int, default=81)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.a is None:
        args.a = 1 / args.q
    if args.q < 2 or not 0 < args.a < 1 or args.sigma <= 0:
        parser.error("Require q >= 2, 0 < a < 1, sigma > 0")
    if args.kind == "symmetric" and not (0 < args.b < np.pi / 2 and args.c > 0
                                         and 2 * args.b * args.c - 1 - args.c**2 / 2 > 0):
        parser.error("Symmetric seed requires 0 < b < pi/2 and 2bc-1-c^2/2 > 0")
    amplitude, integral_data = closing_amplitude(args)
    reference_data = spherical_data(args.q, args.a, args.kind, args.b, args.reference_n)
    reference_speed, _ = speed_data(args, reference_data, amplitude)
    reference_alpha = periodic_primitive(reference_speed[:, None] * reference_data["raw"])
    reference_index = np.arange(0, args.reference_n, max(1, args.reference_n // 2048))
    reference_diameter = sampled_diameter(reference_alpha[reference_index])
    args.fixed_halfwidth = args.width * reference_diameter
    result = dict(schema="literature-band-seed-v1", source="https://arxiv.org/html/2611.17269v1",
                  status="Heuristic numerical band seed; not a closed-surface flex or a reach certificate",
                  parameters={k: v for k, v in vars(args).items() if k != "output"},
                  fixed_amplitude=amplitude, reference_integrals=integral_data,
                  reference_sampled_centerline_diameter=reference_diameter,
                  exact_period_mechanism=("v = V(kappa): Pi is an integral of an exact derivative; "
                                          "q-fold rotation closes horizontal components; A=-I0/I1 closes vertical component"
                                          if args.kind == "curvature" else
                                          "Reflection closes Pi; q-fold rotation and the explicit lambda mean close Lambda"),
                  quadrature=[evaluate(args, n, amplitude) for n in args.n],
                  caveats=["Reference-quadrature A and physical halfwidth are held fixed for all resolutions.",
                           "The Fourier primitive removes the displayed closure residual; no residual is hidden.",
                           "Sampled principal radii are local curvature diagnostics, not lower bounds on reach.",
                           "Centerline and band embedding, global reach, caps, and a continuous fixed-metric flex are unproved."])
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
