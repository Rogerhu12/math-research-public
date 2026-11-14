#!/usr/bin/env python3
"""Targeted M/N diagnosis of the actual circular-warm Lobatto-domain failure.

The complete saved 96-mode core and the same frozen scalar a(s) are used in
every case.  Only the finite rotating-frame representation of its material
circle and its angular quadrature change.  The original finite Frenet RHS
is evaluated at the endpoints; its actual Hermite curve is tested at the
two RMS fractions and at the collocation midpoint.  The saved failed warm
is independently reproduced.  No tail, Newton solve or acceptance is made.

The untruncated material circle is a separate analytic reference.  Its
complete angular derivatives, including all high-frequency contributions,
give kappa=1/a and beta^2=1-a_s^2.  Using its compatible derivatives for a
comparison curve is explicitly not replacing the original finite ODE.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_r225_free_core_bvp as base
from geometry_20261114_full_scalar_profile import read
from geometry_20261114_prefix_controls_profile import reconstruct_profile

HERE = Path(__file__).resolve().parent
FRACTIONS = (.5 - .5 * np.sqrt(3 / 7), .5, .5 + .5 * np.sqrt(3 / 7))
DEFAULT_CASES = ((96, 1024), (96, 2048), (112, 2048), (128, 2048), (160, 4096))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value))) if value.size and np.all(np.isfinite(value)) else None


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    raw = (json.dumps(value, indent=None if path.suffix == ".gz" else 2, allow_nan=False) + "\n").encode()
    temporary.write_bytes(gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw)
    temporary.replace(path)


def make_probe(core, M, N, profile, law):
    if M < len(core) or N <= 4 * M:
        raise ValueError("Retain all saved core modes and resolve every projected frequency")
    padded = np.pad(core, (0, M - len(core)))
    q = base.native.outward.FullCoreProbe(padded, M, N,
        law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    base.fixed.fft.enable_fft(q)
    return q


def circle_arrays(core, N):
    """Exact material circle and its first two WORLD angular derivatives.

The vector components are expressed in the rotating phi frame, just as
q.jet.  Derivatives include the moving frame, with no Fourier truncation.
"""
    phi = 2 * np.pi * np.arange(N) / N
    frequency = 2 * np.arange(1, len(core) + 1)
    cosine = np.cos(frequency[:, None] * phi)
    sine = np.sin(frequency[:, None] * phi)
    density = (1 - frequency ** 2) * core
    delta = (density / frequency) @ sine
    rho = 1 + density @ cosine
    rhop = -(frequency * density) @ sine
    radial = np.column_stack((np.cos(delta), np.sin(delta), np.zeros(N)))
    tangent = np.column_stack((-np.sin(delta), np.cos(delta), np.zeros(N)))
    return radial, rho[:, None] * tangent, rhop[:, None] * tangent - rho[:, None] ** 2 * radial, rho


def geometry(d, dd, a, ap):
    lam2 = np.einsum("ij,ij->i", d, d)
    tangent = d / np.sqrt(lam2)[:, None]
    raw = dd - np.einsum("ij,ij->i", dd, tangent)[:, None] * tangent
    nn = np.sqrt(np.einsum("ij,ij->i", raw, raw))
    curvature = nn / lam2
    beta2 = 1 - (ap / (a * curvature)) ** 2
    at = int(np.argmin(beta2))
    normal = raw / nn[:, None]
    binormal = np.cross(tangent, normal)
    alpha = -ap / (a * curvature)
    with np.errstate(invalid="ignore"):
        velocity = alpha[:, None] * normal + np.sqrt(beta2)[:, None] * binormal
    return dict(minimum_beta_squared=float(beta2[at]),
                minimum_at_phi=float(2 * np.pi * at / len(d)),
                maximum_abs_a_kappa_minus_one=maximum(a * curvature - 1),
                minimum_a_kappa=float(np.min(a * curvature)),
                maximum_a_kappa=float(np.max(a * curvature)),
                minimum_angular_speed=float(np.sqrt(np.min(lam2))),
                finite_domain=bool(np.all(np.isfinite(beta2)) and np.min(beta2) > 0)), velocity


def state_diagnostic(q, profile, s, y, rho):
    a, ap, app = profile.profile(float(s))
    _, d, dd = q.jet(y)
    result, velocity = geometry(d, dd, a, ap)
    result.update(s=float(s), a=float(a), ap=float(ap), app=float(app),
                  exact_circle_beta_squared=float(1 - ap * ap),
                  angular_metric_relative_max=maximum(np.einsum("ij,ij->i", d, d) / (a * rho) ** 2 - 1),
                  nonmean_height_coefficient_max=maximum(y[2 * q.M + 2:]),
                  nonmean_height_second_angular_coefficient_max=maximum(
                      (2 * np.arange(1, q.M + 1)) ** 2 * y[2 * q.M + 2:]))
    return result, velocity


def z_spectrum(values, M):
    """All even angular frequencies present on this actual grid, not just M."""
    N = len(values)
    raw = np.fft.rfft(values)
    frequency = 2 * np.arange(N // 4 + 1)
    amplitudes = (2 / N) * np.abs(raw[frequency])
    amplitudes[0] *= .5
    if N % 4 == 0:
        amplitudes[-1] *= .5
    regions = {}
    for name, lower, upper in (("m1_3", 1, 3), ("m4_32", 4, 32),
                              ("m33_64", 33, 64), ("m65_96", 65, 96),
                              ("retained_above96", 97, M),
                              ("discarded_above_M", M + 1, len(amplitudes) - 1)):
        lower, upper = max(lower, 1), min(upper, len(amplitudes) - 1)
        if lower > upper:
            regions[name] = dict(modes=0, maximum=0., second_angular_weighted_maximum=0.)
        else:
            block = amplitudes[lower:upper + 1]
            weights = frequency[lower:upper + 1] ** 2
            regions[name] = dict(modes=len(block), maximum=float(np.max(block)),
                                second_angular_weighted_maximum=float(np.max(weights * block)))
    return dict(mean=float(raw[0].real / N), groups=regions,
                all_even_amplitudes=amplitudes.tolist(),
                maximum_odd_frequency_amplitude=maximum((2 / N) * raw[1::2]))


def selected_intervals(mesh, report, profile, taper_end):
    labels = {}
    def add(index, label):
        index = int(np.clip(index, 0, len(mesh) - 2))
        if mesh[index] < taper_end:
            return
        labels.setdefault(index, []).append(label)
    first = report["history"][0]
    for check in first["checks"]:
        samples = check.get("first_invalid_points", [])
        if samples:
            prefix = "original_bad_fraction_" + format(check["fraction"], ".9g")
            add(samples[0]["interval"] - 1, prefix + "_preceding")
            for j in sorted(set((0, min(5, len(samples) - 1), len(samples) - 1))):
                sample = samples[j]
                if mesh[sample["interval"]] != sample["left"] or mesh[sample["interval"] + 1] != sample["right"]:
                    raise ValueError("The original bad-query report belongs to another saved mesh")
                add(sample["interval"], prefix + "_sample_" + str(j))
    targets = dict(circle_early=taper_end + .02,
                   circle_turn_middle=(taper_end + profile.turn_end) / 2,
                   turn_late=profile.turn_end - .02,
                   coast_early=profile.turn_end + .02,
                   coast_middle=(profile.turn_end + profile.bridge_start) / 2,
                   coast_late=profile.bridge_start - .02,
                   bridge_early=profile.bridge_start + .2 * (profile.end - profile.bridge_start),
                   bridge_middle=(profile.bridge_start + profile.end) / 2,
                   bridge_late=profile.end - .003)
    for name, s in targets.items():
        add(np.searchsorted(mesh, s, side="right") - 1, name)
    return [dict(index=i, left=float(mesh[i]), right=float(mesh[i + 1]), labels=labels[i])
            for i in sorted(labels)]


def local_height(profile, left, right):
    gx, gw = np.polynomial.legendre.leggauss(24)
    points = [left, *[s for s in profile.knots if left < s < right], right]
    result = 0.
    for a, b in zip(points[:-1], points[1:]):
        speeds = np.array([profile.profile(s)[1] for s in (a + b) / 2 + (b - a) / 2 * gx])
        if np.any(abs(speeds) >= 1):
            raise FloatingPointError("The unchanged scalar profile left |a_s|<1")
        result += (b - a) / 2 * (gw @ np.sqrt(1 - speeds * speeds))
    return float(result)


def hermite_checks(q, profile, x, y, rhs, rho):
    curve = CubicHermiteSpline(x, y, rhs, axis=0)
    checks = []
    for fraction in FRACTIONS:
        s = x[0] + fraction * (x[1] - x[0])
        item, _ = state_diagnostic(q, profile, s, curve(s), rho)
        item["fraction"] = float(fraction)
        checks.append(item)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--warm", type=Path, required=True)
    parser.add_argument("--rms-report", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--case", action="append", help="M,N; repeat to override the five diagnostic defaults")
    parser.add_argument("--taper-fraction", type=float, default=.4)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run numerical probes only in the public repository's own Actions")
    started = time.monotonic()
    warm, failed = read(args.warm), read(args.rms_report)
    M0, N0 = int(warm["M"]), int(warm["N"])
    if (M0, N0) != (96, 1024):
        raise ValueError("This diagnostic is bound to the actual M96/N1024 failed warm")
    n0 = 3 * M0 + 2
    states = np.asarray(warm.get("augmented_states", warm["states"]), float)
    rhs = np.asarray(warm.get("augmented_rhs", warm["rhs"]), float)
    mesh = np.asarray(warm["mesh"], float)
    if states.shape != (len(mesh), n0 + M0 + 3) or rhs.shape != states.shape:
        raise ValueError("Keep every physical, core and control row of the original warm")
    core = states[0, n0:n0 + M0].copy()
    if (not np.all(states[:, n0:n0 + M0] == core) or
            np.any(states[:, -3:] != 0) or np.any(rhs[:, n0:] != 0)):
        raise ValueError("This short circle comparison requires the actual constant core and zero-control seed")
    frozen = reconstruct_profile(warm["complete_scalar_profile"])
    profile = frozen.designed
    if np.any(frozen.frozen_parameters != 0):
        raise ValueError("Do not reinterpret a nonzero solved control vector")
    law = profile.fixed_geometry["initial_law"]
    taper_end = profile.prefix_end + args.taper_fraction * profile.turn.length
    intervals = selected_intervals(mesh, failed, profile, taper_end)
    cases = DEFAULT_CASES if args.case is None else [tuple(map(int, value.split(","))) for value in args.case]
    source_names = (Path(__file__).name, "geometry_20261114_r225_free_core_bvp.py",
        "geometry_20261114_r225_high_core_bvp.py", "geometry_20261114_fft_frenet.py",
        "geometry_20261114_full_scalar_profile.py", "geometry_20261114_prefix_controls_profile.py",
        "geometry_20261114_full_dn_readout.py", "strong_20261114_scaled_core_tail_connector.py",
        "geometry_20261114_r225_fixed_profile.py", "alternative-outward-probe.py", "alternative-neck-provider.py")
    report = dict(schema="targeted-material-circle-domain-probe-v1", scope=__doc__,
        source_repository=os.environ.get("GITHUB_REPOSITORY"), source_commit=os.environ.get("GITHUB_SHA"),
        source_sha256={name: sha(HERE / name) for name in source_names},
        inputs=dict(warm=str(args.warm), warm_sha256=sha(args.warm),
                    rms_report=str(args.rms_report), rms_report_sha256=sha(args.rms_report)),
        original_failure_counts=[dict(nodes=row["nodes"], invalid_RMS_points=row["invalid_RMS_points"])
                                 for row in failed["history"]],
        complete_core_coefficients=core.tolist(), core_modes=M0,
        complete_scalar_profile=warm["complete_scalar_profile"],
        selected_intervals=intervals, taper_end=taper_end,
        original_saved_curve_checks=[], cases=[],
        full_angular_reference=dict(formula="F=a(s)*(cos(Phi_c(phi)),sin(Phi_c(phi)),0)+Z(s)*ez; Z_s=+sqrt(1-a_s^2)",
            angular_derivatives="F_phi=a*rho*e_theta; F_phiphi=a*(rho_phi*e_theta-rho^2*e_radial)",
            curvature="1/a", beta_squared="1-a_s^2", no_angular_mode_discarded=True),
        full_DN_evaluated=False, new_BVP_acceptance=False, continuous_estimate_certified=False)
    q0 = make_probe(core, M0, N0, frozen, law)
    _, _, _, rho0 = circle_arrays(core, N0)
    old_flow = base.BatchedFFTFlow(q0)
    for entry in intervals:
        i = entry["index"]
        x, y, ff = mesh[i:i + 2], states[i:i + 2, :n0], rhs[i:i + 2, :n0]
        actual = old_flow(x, y.T).T
        report["original_saved_curve_checks"].append(dict(interval=entry,
            saved_RHS_replay_max=maximum(actual - ff),
            checks=hermite_checks(q0, frozen, x, y, ff, rho0)))
    write(args.out, report)
    reference_coefficients = {}
    for M, N in cases:
        case_begin = time.monotonic()
        q = make_probe(core, M, N, frozen, law)
        radial, exact_d, exact_dd, rho = circle_arrays(core, N)
        circle = q.project(radial)
        circle[2 * M + 1:] = 0
        _, finite_d, finite_dd = q.jet(circle)
        circle_geo, _ = geometry(finite_d, finite_dd, 1., 0.)
        exact_geo, _ = geometry(exact_d, exact_dd, 1., 0.)
        case = dict(M=M, N=N, retained_original_core_modes=M0, appended_core_modes_are_exact_zero=True,
            complete_material_circle_projection=dict(r= circle[:M + 1].tolist(), t=circle[M + 1:2 * M + 1].tolist()),
            projected_circle_geometry=circle_geo,
            exact_circle_geometry_float_check=exact_geo,
            projected_circle_metric_relative_max=maximum(np.sum(finite_d ** 2, axis=1) / rho ** 2 - 1),
            circle_first_angular_truncation_max=maximum(finite_d - exact_d),
            circle_second_angular_truncation_max=maximum(finite_dd - exact_dd),
            minimum_rho_sample=float(np.min(rho)), intervals=[])
        if M in reference_coefficients:
            priorN, prior = reference_coefficients[M]
            case["same_M_projection_change_from_N"] = dict(N=priorN, maximum=maximum(circle - prior))
        else:
            reference_coefficients[M] = (N, circle.copy())
        flow = base.BatchedFFTFlow(q)
        for entry in intervals:
            left, right = entry["left"], entry["right"]
            x = np.array([left, right])
            jets = np.array([frozen.profile(s) for s in x])
            y = jets[:, :1] * circle[None, :]
            y[1, 2 * M + 1] = local_height(frozen, left, right)
            actual = flow(x, y.T).T
            analytic = jets[:, 1:2] * circle[None, :]
            analytic[:, 2 * M + 1] = np.sqrt(1 - jets[:, 1] ** 2)
            row = dict(interval=entry, original_finite_RHS_all_finite=bool(np.all(np.isfinite(actual))),
                       endpoint_RHS_minus_analytic_circle_derivative_max=maximum(actual - analytic),
                       endpoint_RHS_nonmean_z_max=maximum(actual[:, 2 * M + 2:]),
                       endpoint_RHS_nonmean_z_second_angular_weighted_max=maximum(
                           actual[:, 2 * M + 2:] * (2 * np.arange(1, M + 1)) ** 2),
                       node_diagnostics=[], original_finite_RHS_Hermite=[],
                       analytic_derivative_Hermite_reference=[], untruncated_circle_Hermite_reference=[])
            for j, s in enumerate(x):
                diag, velocity = state_diagnostic(q, frozen, s, y[j], rho)
                if np.all(np.isfinite(velocity)):
                    expected = jets[j, 1] * radial.copy()
                    expected[:, 2] = np.sqrt(1 - jets[j, 1] ** 2)
                    diag.update(complete_velocity_minus_untruncated_circle_max=maximum(velocity - expected),
                                complete_velocity_z_spectrum=z_spectrum(velocity[:, 2], M))
                row["node_diagnostics"].append(diag)
            if np.all(np.isfinite(actual)):
                row["original_finite_RHS_Hermite"] = hermite_checks(q, frozen, x, y, actual, rho)
            row["analytic_derivative_Hermite_reference"] = hermite_checks(q, frozen, x, y, analytic, rho)
            radius_curve = CubicHermiteSpline(x, jets[:, 0], jets[:, 1])
            for fraction in FRACTIONS:
                s = left + fraction * (right - left)
                a, ap, _ = frozen.profile(s)
                radius = float(radius_curve(s))
                row["untruncated_circle_Hermite_reference"].append(dict(fraction=float(fraction), s=float(s),
                    interpolated_radius=radius, scalar_radius=float(a),
                    minimum_beta_squared=float(1 - (ap * radius / a) ** 2),
                    exact_circle_beta_squared=float(1 - ap * ap),
                    maximum_abs_a_kappa_minus_one=float(abs(a / radius - 1))))
            if (M, N) == (M0, N0):
                i = entry["index"]
                saved = states[i:i + 2, :n0].copy()
                saved[:, 2 * M + 1] = y[:, 2 * M + 1]
                row["circle_reconstruction_vs_original_saved_nonmean_state_max"] = maximum(y - saved)
                row["fresh_circle_RHS_vs_original_saved_RHS_max"] = maximum(actual - rhs[i:i + 2, :n0])
            case["intervals"].append(row)
        checks = [item for row in case["intervals"] for item in row["original_finite_RHS_Hermite"]]
        case["summary"] = dict(selected_intervals=len(intervals), Hermite_queries=len(checks),
            invalid_original_finite_RHS_Hermite_queries=sum(not item["finite_domain"] for item in checks),
            minimum_original_finite_RHS_Hermite_beta_squared=min((item["minimum_beta_squared"] for item in checks), default=None),
            maximum_endpoint_nonmean_height_RHS=max((row["endpoint_RHS_nonmean_z_max"] or 0.) for row in case["intervals"]),
            elapsed_seconds=time.monotonic() - case_begin)
        report["cases"].append(case)
        report["elapsed_seconds"] = time.monotonic() - started
        write(args.out, report)
        print(json.dumps(dict(event="material_circle_probe", M=M, N=N, **case["summary"])), flush=True)
    report["completed"] = True
    report["elapsed_seconds"] = time.monotonic() - started
    write(args.out, report)


if __name__ == "__main__":
    main()
