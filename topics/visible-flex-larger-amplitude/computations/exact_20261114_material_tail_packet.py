#!/usr/bin/env python3
"""Convert an accepted complete core to material-angle tail boundary data.

Run numerical work only in this public repository's GitHub Actions.  The
input is an actually accepted BVP, including every core coefficient and
every component of the cut state.  No normal-angle mode is relabelled as a
material-angle mode.  At each requested resolution this program inverts
theta(phi), samples the physical field and its first two derivatives, and
measures finite Fourier truncations against those physical samples.

The output contains finite projected tail requests, the physical boundary
jets they must match, the complete coordinate projection, and its derivative
with respect to every core coefficient at fixed boundary state.  A request
still needs a tail metric and an actual nonlinear DN solve.  In particular,
an outward-going station is useful for spectrum diagnosis but is not the
descending cut used by the existing upper-half assembly.  None of these
sampled calculations certifies an infinite Fourier remainder or closure.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import time
import types

import numpy as np


HERE = Path(__file__).resolve().parent
JET_KEYS = ("F", "F_s", "F_ss", "F_theta", "F_s_theta", "F_theta_theta")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write_json(path, value, compressed=False):
    raw = (json.dumps(value, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":") if compressed else None,
                      indent=None if compressed else 2) + "\n").encode()
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    if len(raw) >= 5_000_000:
        raise ValueError("A result exceeds the repository's single-file limit: " + str(path))
    if not compressed and len(raw) >= 1_000_000:
        raise ValueError("A result larger than 1 MB must be compressed: " + str(path))
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=path.name, bytes=len(raw), sha256=digest(path))


def load_material_helper():
    spec = importlib.util.spec_from_file_location(
        "exact_material_tail_helper", HERE / "geometry_20261114_material_quintic_readout.py")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def source_hashes(helper):
    """Record the actual local modules reached by the helper import chain."""
    pending, seen, answer = [helper], set(), {Path(__file__).name: digest(__file__)}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        path = Path(getattr(module, "__file__", "")).resolve()
        if path.parent != HERE:
            continue
        answer[path.name] = digest(path)
        pending.extend(value for value in vars(module).values() if isinstance(value, types.ModuleType))
    return dict(sorted(answer.items()))


def saved_node_second(q, station, state, saved_rhs):
    """Use precisely the nodal second jet of material_quintic_readout.

    That physical quintic uses the saved first derivative, including when
    differentiating the finite ODE in its state argument.  The difference
    from the freshly evaluated first derivative is reported separately.
    """
    frame = q.frame(float(station), state)
    current_rhs = q.project(frame["V"])
    epsilon = 1e-25
    state_part = q.project(q.frame(float(station), state.astype(complex)
                                  + 1j * epsilon * saved_rhs, strict=False)["V"]).imag / epsilon
    da = -frame["app"] / (frame["a"] * frame["kap"]) + frame["ap"]**2 / (frame["a"]**2 * frame["kap"])
    db = -frame["al"] * da / frame["be"]
    explicit = q.project(da[:, None] * frame["N"] + db[:, None] * frame["B"])
    return state_part + explicit, float(np.max(abs(current_rhs - saved_rhs)))


def station_state(data, q, station):
    mesh = np.asarray(data["mesh"], dtype=float)
    states, rhs = np.asarray(data["states"], dtype=float), np.asarray(data["rhs"], dtype=float)
    if (mesh.ndim != 1 or len(mesh) < 2 or np.any(np.diff(mesh) <= 0)
            or states.shape != (len(mesh), 3 * int(data["M"]) + 2) or rhs.shape != states.shape
            or not np.all(np.isfinite(states)) or not np.all(np.isfinite(rhs))):
        raise ValueError("Expected a complete, ordered, finite accepted BVP state and RHS")
    station = float(mesh[-1] if station is None else station)
    if not mesh[0] <= station <= mesh[-1]:
        raise ValueError("The requested station must belong to the accepted interval")
    exact = np.flatnonzero(mesh == station)
    if len(exact):
        j = int(exact[0])
        second, gap = saved_node_second(q, station, states[j], rhs[j])
        return station, np.array([states[j], rhs[j], second]), dict(
            kind="saved accepted node", node=j, node_count=len(mesh), saved_rhs_gap=gap,
            accepted_interval=[float(mesh[0]), float(mesh[-1])])
    j = int(np.searchsorted(mesh, station) - 1)
    dd0, gap0 = saved_node_second(q, mesh[j], states[j], rhs[j])
    dd1, gap1 = saved_node_second(q, mesh[j+1], states[j+1], rhs[j+1])
    ld = np.longdouble
    h, u = ld(mesh[j+1]) - ld(mesh[j]), (ld(station) - ld(mesh[j])) / (ld(mesh[j+1]) - ld(mesh[j]))
    c0 = states[j].astype(ld)
    c1, c2 = h * rhs[j].astype(ld), h * h * dd0.astype(ld) / 2
    aa = states[j+1].astype(ld) - c0 - c1 - c2
    bb = h * rhs[j+1].astype(ld) - c1 - 2*c2
    cc = h*h*dd1.astype(ld) - 2*c2
    polynomial = np.stack([c0, c1, c2, 10*aa-4*bb+cc/2, -15*aa+7*bb-cc, 6*aa-3*bb+cc/2])
    y = np.polynomial.polynomial.polyval(u, polynomial)
    ys = np.polynomial.polynomial.polyval(u, np.arange(1, 6)[:, None]*polynomial[1:]) / h
    yss = np.polynomial.polynomial.polyval(u, (np.arange(2, 6)*np.arange(1, 5))[:, None]*polynomial[2:]) / h**2
    return station, np.array([y, ys, yss], dtype=float), dict(
        kind="same physical C2 quintic as material_quintic_readout", interval=j,
        interval_bounds=[float(mesh[j]), float(mesh[j+1])], u=float(u), node_count=len(mesh),
        saved_rhs_gap=max(gap0, gap1), accepted_interval=[float(mesh[0]), float(mesh[-1])])


def physical_jets(helper, M, rows, phi, rho, rho_prime):
    value, first, second = helper.angular_jet(None, M, phi)(rows)
    cosine, sine = np.cos(phi), np.sin(phi)

    def rotate(v):
        return np.stack([cosine*v[:, 0]-sine*v[:, 1],
                         sine*v[:, 0]+cosine*v[:, 1], v[:, 2]], axis=1)

    ans = dict(F=rotate(value[0]), F_s=rotate(value[1]), F_ss=rotate(value[2]),
               F_theta=rotate(first[0]/rho[:, None]), F_s_theta=rotate(first[1]/rho[:, None]),
               F_theta_theta=rotate(second[0]/rho[:, None]**2
                                    - first[0]*(rho_prime/rho**3)[:, None]))
    return ans, value, first


def spectrum(values):
    return np.fft.rfft(values, axis=0) / len(values)


def complex_json(values):
    return dict(real=values.real.tolist(), imaginary=values.imag.tolist())


def synthesize(coefficients, count, last_frequency, derivative=0):
    """Evaluate normalized rFFT coefficients without importing a Nyquist bin."""
    last_frequency = min(last_frequency, len(coefficients)-2, count//2-1)
    out = np.zeros((count//2+1,) + coefficients.shape[1:], dtype=complex)
    multiplier = (1j*np.arange(last_frequency+1))**derivative
    multiplier = multiplier.reshape((last_frequency+1,) + (1,)*(coefficients.ndim-1))
    out[:last_frequency+1] = coefficients[:last_frequency+1]*multiplier
    return np.fft.irfft(count*out, n=count, axis=0)


def even_coefficients(values):
    raw = spectrum(values)
    indices = np.arange(0, len(values)//2, 2)  # Deliberately exclude Nyquist.
    cosine, sine = 2*raw[indices].real, -2*raw[indices].imag
    cosine[0] *= .5
    sine[0] = 0
    return cosine, sine


def even_synthesize(cosine, count, modes, derivative=0):
    out = np.zeros((count//2+1,) + cosine.shape[1:], dtype=complex)
    modes = min(modes, len(cosine)-1, (count-1)//4)
    out[2*np.arange(modes+1)] = cosine[:modes+1]/2
    out[0] *= 2
    multiplier = (1j*np.arange(count//2+1))**derivative
    multiplier = multiplier.reshape((count//2+1,) + (1,)*(cosine.ndim-1))
    return np.fft.irfft(count*out*multiplier, n=count, axis=0)


def max_norm(values):
    if values.ndim == 1:
        return float(np.max(abs(values)))
    return float(np.max(np.linalg.norm(values, axis=-1)))


def metric_readout(jets, radius):
    fs, ft = jets["F_s"], jets["F_theta"]
    e = np.sum(fs*fs, axis=1)-1
    f = np.sum(fs*ft, axis=1)/radius
    g = np.sum(ft*ft, axis=1)/radius**2-1
    operator = (abs(e+g) + np.sqrt((e-g)**2+4*f*f))/2
    return dict(component_max=float(np.max(np.maximum.reduce([abs(e), abs(f), abs(g)]))),
                relative_operator_max=float(np.max(operator)),
                minimum_determinant=float(np.min((e+1)*(g+1)-f*f)))


def tail_fields(jets, sign, ap, app):
    fields = {name.replace("F", "H", 1): sign*jets[name][:, 2] for name in JET_KEYS}
    if ap != 0:
        fields.update(H_r=fields["H_s"]/ap,
                      H_rr=fields["H_ss"]/ap**2-app*fields["H_s"]/ap**3,
                      H_r_theta=fields["H_s_theta"]/ap)
    return fields


def sampled_budget(fields, height_cosine, vector_spectra, jets, modes, radius):
    count = len(jets["F"])
    height_sources = {
        "H": ("H", 0), "H_s": ("H_s", 0), "H_ss": ("H_ss", 0),
        "H_theta": ("H", 1), "H_s_theta": ("H_s", 1), "H_theta_theta": ("H", 2)}
    if "H_r" in fields:
        height_sources.update(H_r=("H_r", 0), H_rr=("H_rr", 0), H_r_theta=("H_r", 1))
    height_errors = {key: max_norm(even_synthesize(height_cosine[source], count, modes, order)-fields[key])
                     for key, (source, order) in height_sources.items()}
    scales = dict(H=1/radius, H_s=1., H_ss=radius, H_theta=1/radius,
                  H_s_theta=1., H_theta_theta=1/radius, H_r=1., H_rr=radius, H_r_theta=1.)
    vector_sources = dict(F=("F", 0), F_s=("F_s", 0), F_ss=("F_ss", 0),
                          F_theta=("F", 1), F_s_theta=("F_s", 1), F_theta_theta=("F", 2))
    vector = {key: synthesize(vector_spectra[source], count, 2*modes+1, order)
              for key, (source, order) in vector_sources.items()}
    return dict(tail_modes=modes, vector_max_frequency=2*modes+1,
                tail_worker_minimum_power_of_two_N=1 << (8*modes).bit_length(),
                height_jet_max_abs=height_errors,
                height_scaled_C2_sample_error=max(scales[key]*value for key, value in height_errors.items()),
                F_jet_max_euclidean={key: max_norm(vector[key]-jets[key]) for key in JET_KEYS},
                projected_F_metric_sample=metric_readout(vector, radius))


def material_projection(core, phi, rho, phi_height_jets, sign):
    frequency = 2*np.arange(len(core)+1)
    basis = np.cos(phi[:, None]*frequency[None, :])
    projection, _ = even_coefficients(basis)
    nonzero = frequency[1:]
    phi_derivative = -np.sin(phi[:, None]*nonzero[None, :]) * ((1-nonzero**2)/nonzero)[None, :] / rho[:, None]
    derivatives = {}
    for key, value in zip(("H", "H_s", "H_ss"), phi_height_jets):
        derivatives[key], _ = even_coefficients(sign*value[:, None]*phi_derivative)
    return projection, derivatives, phi_derivative


def finite_difference_core_audit(helper, core, rows, M, count, rho_floor, sign,
                                 analytic, phi_derivative):
    """Independent central differences of the actual inverse map and H."""
    chosen = sorted({1, min(32, len(core)), min(33, len(core)), len(core)})
    rows_out = []
    phi, _, _, _ = helper.material_angles(core, count)
    _, phi_first, _ = helper.angular_jet(None, M, phi)(rows)
    for mode in chosen:
        j, frequency = mode-1, 2*mode
        step = 1e-4*rho_floor/abs(1-frequency**2)
        row = dict(core_mode=mode, nominal_step=float(step), trials=[])
        for factor in (1., .5):
            plus, minus = core.copy(), core.copy()
            plus[j] += step*factor
            minus[j] -= step*factor
            denominator = float(plus[j]-minus[j])
            if denominator == 0:
                raise ValueError("Core derivative finite-difference step is not representable")
            pp, pr, _, pi = helper.material_angles(plus, count)
            mp, mr, _, mi = helper.material_angles(minus, count)
            pv = helper.angular_jet(None, M, pp)(rows)[0]
            mv = helper.angular_jet(None, M, mp)(rows)[0]
            hdiff = sign*(pv[:, :, 2]-mv[:, :, 2])/denominator
            phi_error = float(np.max(abs((pp-mp)/denominator-phi_derivative[:, j])))
            errors = {}
            for index, name in enumerate(("H", "H_s", "H_ss")):
                dc, _ = even_coefficients(hdiff[index])
                direct = sign*phi_first[index, :, 2]*phi_derivative[:, j]
                errors[name] = dict(
                    coefficient_max_abs=float(np.max(abs(dc-analytic[name][:, j]))),
                    physical_field_max_abs=float(np.max(abs(hdiff[index]-direct))),
                    physical_field_relative=float(np.max(abs(hdiff[index]-direct))/max(1., np.max(abs(direct)))))
            row["trials"].append(dict(actual_denominator=denominator, phi_derivative_max_abs=phi_error,
                                      minimum_perturbed_density=float(min(pr.min(), mr.min())),
                                      maximum_inverse_residual=max(pi["max_angle_residual"], mi["max_angle_residual"]),
                                      derivatives=errors))
        rows_out.append(row)
    return rows_out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--station", type=float, help="Physical s; default is the accepted endpoint")
    parser.add_argument("--angles", type=int, nargs="+", default=[1024, 2048, 4096])
    parser.add_argument("--tail-modes", type=int, nargs="+", default=[16, 32, 64, 96, 128, 192, 256, 384, 512, 768])
    parser.add_argument("--native-height-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument("--jet-tolerance", type=float, default=1e-8)
    parser.add_argument("--out", type=Path, required=True, help="Fresh output directory")
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise ValueError("Numerical execution belongs to Rogerhu12/math-research-public GitHub Actions")
    started = time.monotonic()
    data = read_json(args.input)
    if data.get("success") is not True:
        raise ValueError("A genuinely accepted complete BVP is required")
    M, N = int(data["M"]), int(data["N"])
    core = np.asarray(data["core"]["coefficients"], dtype=float)
    if core.shape != (M,) or not np.all(np.isfinite(core)):
        raise ValueError("The complete accepted core must have M finite coefficients")
    counts, budgets = sorted(set(args.angles)), sorted(set(args.tail_modes))
    if (len(counts) < 2 or any(n < 4*(M+1) or n & (n-1) for n in counts)
            or any(m < 1 for m in budgets) or not budgets or args.jet_tolerance <= 0):
        raise ValueError("Use at least two powers-of-two angle grids resolving the original core, positive budgets and tolerance")
    if budgets[-1] >= counts[-1]//4:
        raise ValueError("The largest requested material mode must lie strictly below finest-grid Nyquist")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise ValueError("Use a fresh output directory")
    helper = load_material_helper()
    law = data["original_metric_identity"]["law"]
    q = helper.base.native.outward.FullCoreProbe(core, M, N, law["velocity"], law["length"], law["k0"])
    fixed = helper.base.fixed.FixedProfile(data["fixed_scalar_profile"]["geometry"])
    q.profile = fixed.profile
    helper.base.fixed.fft.enable_fft(q)
    station, rows, state_info = station_state(data, q, args.station)
    radius, ap, app = map(float, q.profile(station))
    if radius <= 0 or not np.all(np.isfinite([radius, ap, app])):
        raise ValueError("The selected station must have a positive finite metric radius")
    sign = args.native_height_sign
    radial_reference = None
    if 0 < abs(ap) < 1:
        w = float(np.sqrt(1-ap*ap)/abs(ap))
        background_sign = sign*int(np.sign(ap))
        radial_reference = dict(E=1/ap**2, w=w, w_r=-app/(w*ap**4),
                                radial_orientation=int(np.sign(ap)), sqrt_E=1/abs(ap),
                                convention="Axisymmetric reference takes physical Z_s=+sqrt(1-a_s^2).",
                                native_background_slope_sign=background_sign,
                                signed_w=background_sign*w, signed_w_r=-background_sign*app/(w*ap**4),
                                positive_native_w_factory_orientation_compatible=background_sign > 0)
    physical_identity = dict(
        accepted_core_coefficients_rational=[str(Fraction(float(value))) for value in core],
        scalar_initial_law=data["fixed_scalar_profile"]["geometry"]["initial_law"],
        scalar_exact_polynomial_sha256=fixed.exact_coefficient_sha256,
        scalar_knots=data["fixed_scalar_profile"]["geometry"]["knots"])
    physical_identity_sha256 = helper.base.fixed.canonical_hash(physical_identity)
    artifacts, levels, internals = [], [], []
    density_coefficients = (1-(2*np.arange(1, M+1))**2)*core
    density_second_bound = float(np.sum((2*np.arange(1, M+1))**2*abs(density_coefficients)))
    for count in counts:
        phi, rho, rho_prime, inverse_info = helper.material_angles(core, count)
        if np.min(rho) <= 0:
            raise ValueError("The sampled material density is not positive")
        jets, value, first = physical_jets(helper, M, rows, phi, rho, rho_prime)
        vectors = {key: spectrum(jets[key]) for key in ("F", "F_s", "F_ss")}
        fields = tail_fields(jets, sign, ap, app)
        plain_fields = [key for key in fields if "theta" not in key]
        cosines, sines = {}, {}
        for key in plain_fields:
            cosines[key], sines[key] = even_coefficients(fields[key])
        uniform_phi = 2*np.pi*np.arange(count)/count
        uniform_density = 1 + density_coefficients@np.cos(2*np.arange(1, M+1)[:, None]*uniform_phi)
        uniform_first = helper.angular_jet(None, M, uniform_phi)(rows)[1][0]
        theta_speed = np.linalg.norm(jets["F_theta"], axis=1)
        phi_speed = np.linalg.norm(uniform_first, axis=1)
        if uniform_density.min() <= 0:
            raise ValueError("The independently sampled original-angle density is not positive")
        length = dict(
            target=2*np.pi*radius, material_angle_quadrature=float(2*np.pi*np.mean(theta_speed)),
            original_angle_quadrature=float(2*np.pi*np.mean(phi_speed)),
            material_speed_relative_error=float(np.max(abs(theta_speed/radius-1))),
            original_speed_relative_error=float(np.max(abs(phi_speed/(radius*uniform_density)-1))),
            density_uniform_min=float(uniform_density.min()), density_uniform_max=float(uniform_density.max()),
            density_mean_error=float(abs(np.mean(uniform_density)-1)),
            density_triangle_lower=float(1-np.sum(abs(density_coefficients))),
            density_grid_lower_estimate=float(uniform_density.min()-density_second_bound*(2*np.pi/count)**2/8),
            density_lower_estimate_is_outward_rounded_certificate=False)
        length["relative_material_length_error"] = abs(length["material_angle_quadrature"]/length["target"]-1)
        length["relative_original_length_error"] = abs(length["original_angle_quadrature"]/length["target"]-1)
        projection, core_derivatives, phi_derivative = material_projection(core, phi, rho, first[:, :, 2], sign)
        compatible_budgets = [m for m in budgets if m < count//4]
        budget_rows = [sampled_budget(fields, cosines, vectors, jets, m, radius) for m in compatible_budgets]
        angular_frequencies = np.arange(count//2+1)
        hspec = spectrum(fields["H"])
        forbidden = np.ones(len(hspec), dtype=bool)
        forbidden[::2] = False
        parity = dict(odd_frequency_amplitude_max=float(2*np.max(abs(hspec[forbidden]))),
                      even_sine_amplitude_max=float(np.max(abs(sines["H"]))),
                      excluded_nyquist_cosine=float(hspec[-1].real),
                      excluded_nyquist_second_derivative_amplitude=float(abs(hspec[-1])*angular_frequencies[-1]**2))
        circle = np.stack([radius*np.cos(uniform_phi), radius*np.sin(uniform_phi)], axis=1)
        level = dict(angles=count, material_modes_available=count//4-1,
                     angle_inversion=inverse_info, length_density=length,
                     physical_metric_sample=metric_readout(jets, radius),
                     physical_jet_max={key: max_norm(jets[key]) for key in JET_KEYS},
                     fixed_gauge_xy_mean=jets["F"][:, :2].mean(axis=0).tolist(),
                     fixed_gauge_circle_deviation_sample=float(np.max(np.linalg.norm(jets["F"][:, :2]-circle, axis=1))),
                     height_parity=parity, budgets=budget_rows,
                     projection_constant_column_error=float(np.max(abs(projection[:, 0]-np.eye(len(projection), 1)[:, 0]))),
                     theta_height_from_projection_gap=float(np.max(abs(projection@rows[0, 2*M+1:]-sign*cosines["H"]))))
        spectrum_packet = dict(
            schema="complete-material-angle-spectrum-v1", angles=count, station=station,
            fourier_convention="a_k=rfft(f)_k/N; f(theta)=a_0+2 Re sum_{0<k<N/2} a_k exp(ik theta)+a_N/2 cos(N theta/2).",
            vector_components=["x", "y", "z"], vectors={key: complex_json(value) for key, value in vectors.items()},
            height_convention="H=epsilon_h Z. Arrays index m and multiply cos(2m theta) or sin(2m theta); index zero is the actual mean. Nyquist is excluded and reported separately.",
            native_height_sign=sign, height_cosine={key: value.tolist() for key, value in cosines.items()},
            height_sine={key: value.tolist() for key, value in sines.items()},
            original_material_angle_phi=phi.tolist(), original_density_at_phi=rho.tolist(),
            infinite_Fourier_remainder_certified=False)
        artifacts.append(write_json(out/f"spectrum-N{count}.json.gz", spectrum_packet, True))
        levels.append(level)
        internals.append(dict(count=count, jets=jets, fields=fields, vectors=vectors, cosines=cosines,
                              projection=projection, core_derivatives=core_derivatives,
                              phi_derivative=phi_derivative, phi=phi, rho=rho,
                              uniform_density=uniform_density))
        print(json.dumps(dict(event="material_tail_spectrum", angles=count, station=station,
                              metric=level["physical_metric_sample"], density_min=length["density_uniform_min"],
                              tail_budgets=[dict(M=row["tail_modes"], error=row["height_scaled_C2_sample_error"])
                                            for row in budget_rows], seconds=time.monotonic()-started)), flush=True)

    finest = internals[-1]
    fine_count = finest["count"]
    comparisons = []
    vector_sources = dict(F=("F", 0), F_s=("F_s", 0), F_ss=("F_ss", 0),
                          F_theta=("F", 1), F_s_theta=("F_s", 1), F_theta_theta=("F", 2))
    for lower in internals[:-1]:
        last_frequency = lower["count"]//2-1
        common_modes = lower["count"]//4-1
        comparison = dict(
            source_angles=lower["count"], target_angles=fine_count, common_height_modes=common_modes,
            common_vector_coefficient_max_abs={key: float(np.max(abs(lower["vectors"][key][:-1]-finest["vectors"][key][:last_frequency+1])))
                                               for key in lower["vectors"]},
            complete_lower_grid_F_jets_on_finest={key: max_norm(synthesize(lower["vectors"][source], fine_count, last_frequency, order)-finest["jets"][key])
                                                for key, (source, order) in vector_sources.items()},
            common_height_coefficient_max_abs={key: float(np.max(abs(lower["cosines"][key]-finest["cosines"][key][:common_modes+1])))
                                               for key in lower["cosines"]},
            projection_common_coefficient_max_abs=float(np.max(abs(lower["projection"]-finest["projection"][:common_modes+1]))),
            core_map_derivative_common_max_abs={key: float(np.max(abs(lower["core_derivatives"][key]-finest["core_derivatives"][key][:common_modes+1])))
                                                for key in lower["core_derivatives"]},
            budgets_on_finest=[])
        for modes in budgets:
            if modes > common_modes:
                continue
            result = sampled_budget(finest["fields"], lower["cosines"], lower["vectors"], finest["jets"], modes, radius)
            comparison["budgets_on_finest"].append(result)
        comparisons.append(comparison)

    mode_cap = budgets[-1]
    matrix_common = dict(angles=fine_count, station=station, output_modes=list(range(mode_cap+1)),
                         input_core_modes=list(range(1, M+1)), native_height_sign=sign,
                         held_original_phi_jet_vectors=["y", "saved y_s", "physical y_ss"],
                         coordinate_contribution_only=True, fixed_scalar_profile=True,
                         scope="Finite trapezoidal Fourier projection. Full core coordinate variation is retained; no infinite remainder certificate.")
    artifacts.append(write_json(out/"material-projection.json.gz", dict(
        **matrix_common, schema="complete-material-angle-projection-v1",
        input_phi_cosine_modes=list(range(M+1)),
        definition="P[m,j]=cosine coefficient m in theta of cos(2j phi(theta)); P[0,j] is the actual material mean.",
        values=finest["projection"][:mode_cap+1].tolist()), True))
    for key, value in finest["core_derivatives"].items():
        artifacts.append(write_json(out/f"core-map-derivative-{key}.json.gz", dict(
            **matrix_common, schema="complete-material-angle-core-derivative-v1", field=key,
            definition="At fixed original-phi jet vectors, dphi/dc_j=-(1-4j^2)sin(2j phi)/(2j rho); derivative of H is epsilon_h Z_phi dphi/dc_j, and similarly for held s jets. State, finite-ODE, and scalar-control derivative contributions to the full BC Jacobian must also be included.",
            values=value[:mode_cap+1].tolist()), True))
    derivative_audit = finite_difference_core_audit(
        helper, core, rows, M, fine_count, float(min(finest["rho"].min(), finest["uniform_density"].min())),
        sign, finest["core_derivatives"], finest["phi_derivative"])

    requests = []
    for modes in budgets:
        request = dict(id=f"material-N{fine_count}-M{modes}",
                       height=finest["cosines"]["H"][1:modes+1].tolist(), jacobian=True, audit=True)
        metadata = write_json(out/f"tail-request-M{modes}.json", request)
        requests.append(dict(**metadata, M=modes, N_minimum=1 << (8*modes).bit_length(),
                             boundary_mean_height=float(finest["cosines"]["H"][0]),
                             actual_tail_metric_still_required=True, nonlinear_DN_solve_performed=False))
    boundary_packet = dict(
        schema="complete-material-angle-tail-boundary-v1", input_sha256=digest(args.input),
        station=station, radius=radius, a_s=ap, a_ss=app, native_height_sign=sign,
        radial_reference=radial_reference, original_phi_M=M, original_angular_N=N,
        original_core_coefficients=core.tolist(), original_cut_state=rows[0].tolist(),
        original_cut_saved_first_derivative=rows[1].tolist(), original_cut_physical_second_derivative=rows[2].tolist(),
        physical_identity=physical_identity, physical_identity_sha256=physical_identity_sha256,
        material_modes_stored=fine_count//4-1, material_grid=fine_count,
        native_boundary_cosine={key: value.tolist() for key, value in finest["cosines"].items()},
        profile_geometry=data["fixed_scalar_profile"]["geometry"],
        mean_convention="Native H=epsilon_h Z. Worker height excludes only its mean; actual mean height and mean first/second jets are retained here. No mean slope is reset.",
        radial_convention="r=a(s), H_r=H_s/a_s, H_rr=H_ss/a_s^2-a_ss H_s/a_s^3. Existing upper-half assembly uses epsilon_h=-1 and a_s<0.",
        boundary_residual_convention="Z_s^theta-epsilon_h epsilon_r D(epsilon_h Z^theta)/sqrt(E), epsilon_r=sign(a_s), E=1/a_s^2, for a compatible actual native DN map D.",
        map_derivative_files=[row for row in artifacts if row["file"].startswith("core-map-")],
        projection_file=next(row for row in artifacts if row["file"].startswith("material-projection")),
        worker_requests=requests, complete_tail_matching=False, infinite_Fourier_remainder_certified=False)
    artifacts.append(write_json(out/"tail-boundary-packet.json.gz", boundary_packet, True))
    artifacts.extend(requests)
    candidates = [row["tail_modes"] for row in levels[-1]["budgets"]
                  if row["height_scaled_C2_sample_error"] <= args.jet_tolerance]
    converged_candidates = []
    for modes in candidates:
        applicable = [row for item in comparisons for row in item["budgets_on_finest"] if row["tail_modes"] == modes]
        if applicable and applicable[-1]["height_scaled_C2_sample_error"] <= args.jet_tolerance:
            converged_candidates.append(modes)
    try:
        revision = subprocess.check_output(["git", "-C", str(HERE), "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    summary = dict(
        schema="complete-material-angle-tail-audit-v1", scope=__doc__, public_commit=revision,
        input_sha256=digest(args.input), sources=source_hashes(helper), accepted_input=True,
        M=M, original_angular_N=N, station=station, scalar_jet=dict(a=radius, a_s=ap, a_ss=app),
        physical_identity_sha256=physical_identity_sha256,
        state_readout=state_info, native_height_sign=sign, radial_reference=radial_reference,
        material_map="theta=phi+sum_j (1-4j^2)c_j sin(2j phi)/(2j), rho=dtheta/dphi; every accepted c_j is retained.",
        material_angle_is_constant_along_meridian=True,
        physical_field_definition="Same accepted-nodal C2 quintic as geometry_20261114_material_quintic_readout.py; derivatives are transformed before Fourier truncation.",
        levels=levels, angular_grid_comparisons=comparisons, core_map_derivative_finite_difference=derivative_audit,
        budget_criterion=dict(tolerance=args.jet_tolerance,
                             definition="max(|dH|/a, |dH_theta|/a, |dH_thetatheta|/a, |dH_s|, |dH_stheta|, a|dH_ss|; also radial jets where a_s!=0), sampled on the finest grid.",
                             finest_grid_passing_modes=candidates,
                             passing_on_finest_from_at_least_two_grids=converged_candidates,
                             smallest_tested_two_grid_budget=min(converged_candidates) if converged_candidates else None,
                             mathematical_mode_sufficiency_certified=False),
        existing_upper_half_cut_orientation_compatible=bool(ap < 0 and sign == -1),
        actual_tail_metric_supplied=False, actual_tail_DN_solved=False, complete_tail_matching=False,
        continuous_metric_certificate=False, continuous_embedding_or_reach_certificate=False,
        closed_surface=False, task_completed=False, numerical_readout_complete=True,
        artifacts=artifacts, seconds=time.monotonic()-started)
    write_json(out/"summary.json", summary)
    print(json.dumps(dict(event="material_tail_packet_complete", station=station,
                          out=str(out), budget_criterion=summary["budget_criterion"],
                          existing_upper_half_cut_orientation_compatible=summary["existing_upper_half_cut_orientation_compatible"],
                          seconds=summary["seconds"], task_completed=False)), flush=True)


if __name__ == "__main__":
    main()
