#!/usr/bin/env python3
"""R571 phase shooting to a genuine C2 cylindrical connector.

One fixed milder tail is evaluated at phase zero with M/tolerance comparisons.
Then phase is varied as a DESIGN parameter to solve the actual core C=0
condition. A fixed explicit C2 connector is used, and the selected true
linear field is normalized to A_core=1 before C2 costs are reported.
Modes 4,6,8 are finite numerical probes only; R571 proves mode 2, not an
all-frequency nonlinear inverse. No finite isometric family is claimed.
"""
import argparse
from dataclasses import asdict, dataclass
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import beta as beta_function

SEED_SHA256 = "ede50d8c4d362d77f9618b3481233d32e5ecc73842af7d84dddd8c78bb518970"
SEED_PATH = Path(__file__).with_name("r571_milder_seed_outer_jets_20261126.py")
if hashlib.sha256(SEED_PATH.read_bytes()).hexdigest() != SEED_SHA256:
    raise RuntimeError("R571 shooting requires its explicitly bound seed source")
import r571_milder_seed_outer_jets_20261126 as seed

SCHEMA = "r571-phase-core-shooting-and-unit-core-C2-v1"
RHS_COUNTS = {"seed": 0, "connector": 0}


def emit(tag, obj):
    print(tag + " " + json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                allow_nan=False), flush=True)


@dataclass(frozen=True)
class Connector:
    core_radius: float = .38
    tail_radius: float = .30
    alpha: float = .55
    beta: float = 1.1
    scale: float = 1.0
    core_half_height: float = .04
    reach_target: float = .061

    @property
    def d(self):
        return self.core_radius - self.tail_radius

    @property
    def m(self):
        return 1 / (1 - self.alpha)


def tail_w(r, phase):
    delta = (np.asarray(r) - seed.RC) / seed.ELL
    u = 1 / delta
    angle = u + phase
    w = seed.AMP * np.exp(-(2 - np.sin(angle)) * u)
    wr = w * ((2 - np.sin(angle)) * u ** 2 - np.cos(angle) * u ** 3) / seed.ELL
    return w, wr


def meridian(x, phase, par):
    x = np.asarray(x, dtype=float)
    m, d = par.m, par.d
    y = x ** m
    t = np.maximum(1 - y, 0)
    a = par.core_radius - d * y
    ax = -d * m * x ** (m - 1)
    axx = -d * m * (m - 1) * x ** (m - 2)
    w, wr = tail_w(a, phase)
    # b(r)=scale*t^beta/(1-t^2)^alpha, where t=(r-r0)/d.
    # In x coordinates t=1-x^m. m(1-alpha)=1 removes the core singularity.
    B = d * m * par.scale * t ** par.beta / (2 - y) ** par.alpha
    Bx = d * m * par.scale * m * x ** (m - 1) * (
        -par.beta * t ** (par.beta - 1) / (2 - y) ** par.alpha
        + par.alpha * t ** par.beta / (2 - y) ** (par.alpha + 1))
    zx = B - ax * w
    zxx = Bx - axx * w - ax * ax * wr
    return a, ax, axx, zx, zxx


def field_rhs(x, state, phase, par, j):
    RHS_COUNTS["connector"] += 1
    a, ax, _, zx, _ = meridian(x, phase, par)
    if not zx > 0:
        raise ArithmeticError("regular connector lost positive vertical speed")
    A, C = state
    Ap = -(j * j - 1) * ax / a * A - j * j * zx / a * C
    Cp = -ax / zx * Ap
    return [Ap, Cp]


def connector_field(tail_values, phase, par, j, rtol, atol):
    incoming = np.asarray([tail_values[-1, 4], tail_values[-1, 0]])
    result = solve_ivp(lambda x, y: field_rhs(x, y, phase, par, j),
                       (1.0, 0.0), incoming, method="DOP853",
                       rtol=rtol, atol=atol, max_step=.02, dense_output=True)
    if not result.success or not np.all(np.isfinite(result.y[:, -1])):
        raise ArithmeticError("connector linear transfer failed: " + str(result.message))
    A, C = result.y[:, -1]
    norm = math.hypot(float(A), float(C))
    if not norm > 0:
        raise ArithmeticError("nonzero field was lost in connector transfer")
    return {"solution": result, "A_core": float(A), "C_core": float(C),
            "C_core_over_norm": float(C / norm),
            "C_core_over_A": float(C / A) if A != 0 else None,
            "nfev_connector": int(result.nfev)}


def seed_summary(coarse, fine, nextM):
    common = fine["profile"]["outer_cauchy_log_norm"]
    values = seed.display_profile(fine["profile"], common)
    peaks = []
    for j, name in enumerate(seed.JET_NAMES):
        index = int(np.argmax(np.abs(values[:, j])))
        peaks.append({"field": name, "value": float(values[index, j]),
                      "r": float(fine["profile"]["radii"][index])})
    table = {"r": fine["profile"]["radii"].tolist(), "jets": values.tolist()}
    raw = json.dumps(table, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return {"common_display_log_scale": common,
            "outer_jet_names": seed.JET_NAMES,
            "outer_jets": values[-1].tolist(), "sampled_peaks": peaks,
            "tolerance_comparison": seed.comparison(coarse, fine, common),
            "M_plus_1_comparison": seed.comparison(fine, nextM, common),
            "recomputable_table_JSON_bytes": len(raw),
            "recomputable_table_SHA256": hashlib.sha256(raw).hexdigest(),
            "table_not_persisted_or_uploaded": True}


def cap_height(phase, par):
    delta_max = (par.core_radius - seed.RC) / seed.ELL
    cut = .03
    umin, umax = 1 / delta_max, 1 / cut
    k0 = int(np.ceil((umin + phase) / (np.pi / 2)))
    k1 = int(np.floor((umax + phase) / (np.pi / 2)))
    u = np.arange(k0, k1 + 1) * (np.pi / 2) - phase
    points = 1 / u[(u > umin) & (u < umax)]
    value, error = quad(lambda delta: seed.AMP * seed.ELL
                        * np.exp(-(2 - np.sin(1 / delta + phase)) / delta),
                        cut, delta_max, points=np.sort(points),
                        epsabs=1e-13, epsrel=1e-12, limit=400)
    connector_b_integral = par.scale * par.d / 2 * beta_function(
        (par.beta + 1) / 2, 1 - par.alpha)
    omitted = seed.AMP * seed.ELL * cut * np.exp(-1 / cut)
    return float(par.core_half_height + value + connector_b_integral), {
        "QUADPACK_error_estimate_not_certificate": float(error),
        "rigorous_omitted_flat_height_upper_bound": float(omitted)}


def field_norms(a, A, C, As, Cs, Ass, Css, j):
    return {
        "V": np.hypot(A, C),
        "V_s": np.hypot(As, Cs),
        "V_ss": np.hypot(Ass, Css),
        "V_theta_over_a": np.sqrt((j - 1 / j) ** 2 * A * A + j * j * C * C) / a,
        "V_s_theta_over_a": np.sqrt((j - 1 / j) ** 2 * As * As + j * j * Cs * Cs) / a,
        "V_theta_theta_over_a2": np.sqrt((j * j - 1) ** 2 * A * A + j ** 4 * C * C) / (a * a),
    }


def peak_records(values, positions, label):
    rows = []
    for name, field in values.items():
        index = int(np.argmax(np.abs(field)))
        rows.append({"field": name, "absolute_max": float(abs(field[index])),
                     label: float(positions[index]), "index": index})
    return rows


def full_field_report(item, phase, par, j, nodes):
    common = item["seed"]["profile"]["outer_cauchy_log_norm"]
    values = seed.display_profile(item["seed"]["profile"], common)
    Acore = item["connector"]["A_core"]
    if Acore == 0:
        raise ArithmeticError("A_core normalization is singular")
    values = values / Acore
    radii = item["seed"]["profile"]["radii"]
    w, wr = tail_w(radii, phase)
    E = 1 + w * w
    A, Ar, Arr = values[:, 4], values[:, 5], values[:, 6]
    C, Cr, Crr = values[:, 0], values[:, 1], values[:, 2]
    tail_norms = field_norms(radii, A, C, Ar / np.sqrt(E), Cr / np.sqrt(E),
                            Arr / E - Ar * w * wr / E ** 2,
                            Crr / E - Cr * w * wr / E ** 2, j)
    near = 10.0 ** -np.arange(1, 13)
    x = np.unique(np.r_[np.linspace(0, 1, nodes), near, 1 - near])
    A, C = item["connector"]["solution"].sol(x) / Acore
    a, ax, axx, zx, zxx = meridian(x, phase, par)
    E = ax * ax + zx * zx
    Ex = 2 * ax * axx + 2 * zx * zxx
    P = -(j * j - 1) * ax / a
    Q = -j * j * zx / a
    H = -ax / zx
    Px = -(j * j - 1) * (axx / a - ax * ax / a ** 2)
    Qx = -j * j * (zxx / a - zx * ax / a ** 2)
    Hx = -axx / zx + ax * zxx / zx ** 2
    Ax = P * A + Q * C
    Cx = H * Ax
    Axx = Px * A + P * Ax + Qx * C + Q * Cx
    Cxx = Hx * Ax + H * Axx
    connector_norms = field_norms(
        a, A, C, Ax / np.sqrt(E), Cx / np.sqrt(E),
        Axx / E - Ax * Ex / (2 * E ** 2),
        Cxx / E - Cx * Ex / (2 * E ** 2), j)
    km = (ax * zxx - zx * axx) / E ** 1.5
    kt = zx / (a * np.sqrt(E))
    height, quadrature = cap_height(phase, par)
    return {
        "normalization": "same true field divided by its signed A_core; A_core=1",
        "A_core_before_normalization": Acore,
        "C_core_after_normalization": item["connector"]["C_core"] / Acore,
        "tail_peaks": peak_records(tail_norms, radii, "r"),
        "connector_peaks": peak_records(connector_norms, x, "x"),
        "geometry": {
            "connector_principal_curvature_observed_max": float(max(np.max(abs(km)), np.max(abs(kt)))),
            "connector_principal_curvature_attainers": peak_records({"meridional": km, "parallel": kt}, x, "x"),
            "connector_reach_target_curvature_product_observed_max": float(
                par.reach_target * max(np.max(abs(km)), np.max(abs(kt)))),
            "positive_meridian_E_observed_min": float(np.min(E)),
            "E_is_coordinate_dependent_not_a_reparametrization_invariant_thickness": True,
            "cap_height": height, "enclosing_ball_radius_upper_bound": float(math.hypot(par.core_radius, height)),
            "cylinder_radius": par.core_radius, "cap_height_quadrature": quadrature,
            "all_pair_reach_not_checked": True,
        },
        "tail_inner_unsampled_interval": [seed.RC, float(radii[0])],
        "C2_is_reported_in_meridional_arclength_and_scaled_angular_coordinate_derivatives": True,
        "curvature_and_field_peaks_are_finite_sampling_observations": True,
        "complete": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--M", type=int, default=25)
    parser.add_argument("--radial-nodes", type=int, default=257)
    parser.add_argument("--connector-nodes", type=int, default=4097)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.10)
    parser.add_argument("--tolerance-refinement", type=float, default=8)
    parser.add_argument("--phase-xtol", type=float, default=2e-8)
    parser.add_argument("--phase-derivative-step", type=float, default=1e-5)
    parser.add_argument("--connector-alpha", type=float, default=.55)
    parser.add_argument("--connector-beta", type=float, default=1.1)
    parser.add_argument("--connector-scale", type=float, default=1.0)
    args = parser.parse_args()
    par = Connector(alpha=args.connector_alpha, beta=args.connector_beta, scale=args.connector_scale)
    if not (.5 < par.alpha < 1 and par.beta > 1 and par.scale > 0):
        raise ValueError("C2 connector requires 1/2<alpha<1, beta>1, positive scale")
    started = time.monotonic()
    original_seed_rhs = seed.rhs

    def counted_seed_rhs(u, state):
        RHS_COUNTS["seed"] += 1
        return original_seed_rhs(u, state)

    seed.rhs = counted_seed_rhs
    definition = {
        "schema": SCHEMA, "arguments": vars(args), "connector": asdict(par),
        "seed_source_sha256": SEED_SHA256,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixed_tail_family": "R571 A=.8, rc=.22, ell=.2, sin(delta^-1+phase)",
        "connector_graph_slope": "w_phase(r)+scale*t^beta/(1-t^2)^alpha; t=(r-.30)/(.38-.30)",
        "connector_regular_parameter": "r=.38-.08*x^(1/(1-alpha)), 0<=x<=1",
        "C2_matching": "core r_x=r_xx=z_xx=0; at tail extra z_x and z_xx vanish for beta>1",
        "phase_is_a_design_parameter_not_the_final_isometric_motion": True,
        "theorem_seed_and_shooting_scope": "mode 2 only",
        "higher_modes_4_6_8_are_finite_numerical_probes_not_all_frequency_inverse": True,
        "raw_arrays_or_tables_are_not_persisted": True, "complete": False,
    }
    emit("R571_SHOOTING_DEFINITION", definition)
    fine_rtol, fine_atol = args.rtol / args.tolerance_refinement, args.atol / args.tolerance_refinement
    seed.PHASE, seed.ANGULAR_MODE = 0.0, 2
    coarse = seed.calculate(args.M, args.rtol, args.atol, args.max_step, args.radial_nodes)
    fine = seed.calculate(args.M, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    nextM = seed.calculate(args.M + 1, fine_rtol, fine_atol, args.max_step, args.radial_nodes)
    emit("R571_PHASE_ZERO_SEED", seed_summary(coarse, fine, nextM))
    cache = {}
    nfev_seed = sum(run["inner"]["nfev_inner"] + run["profile"]["nfev_outer"]
                   for run in (coarse, fine, nextM))
    nfev_connector = 0

    def evaluate(phase, j=2, M=None, rtol=None, atol=None):
        nonlocal nfev_seed, nfev_connector
        M = args.M if M is None else M
        rtol = fine_rtol if rtol is None else rtol
        atol = fine_atol if atol is None else atol
        key = (float(phase), j, M, rtol, atol)
        if key in cache:
            return cache[key]
        seed.PHASE, seed.ANGULAR_MODE = float(phase), j
        reused_phase_zero = phase == 0 and j == 2 and M == args.M and rtol == fine_rtol and atol == fine_atol
        if reused_phase_zero:
            run = fine
        else:
            run = seed.calculate(M, rtol, atol, args.max_step, args.radial_nodes)
            nfev_seed += run["inner"]["nfev_inner"] + run["profile"]["nfev_outer"]
        values = seed.display_profile(run["profile"], run["profile"]["outer_cauchy_log_norm"])
        connector = connector_field(values, phase, par, j, rtol, atol)
        nfev_connector += connector["nfev_connector"]
        item = {"seed": run, "connector": connector}
        cache[key] = item
        emit("R571_PHASE_EVALUATION", {
            "phase": phase, "angular_mode": j, "M": M, "rtol": rtol, "atol": atol,
            "A_core": connector["A_core"], "C_core": connector["C_core"],
            "C_core_over_norm": connector["C_core_over_norm"], "C_core_over_A": connector["C_core_over_A"],
            "alpha_first": run["inner"]["alpha_first"], "rho_first_plus_one": run["inner"]["rho_first_plus_one"],
            "nfev_seed": run["inner"]["nfev_inner"] + run["profile"]["nfev_outer"],
            "reused_already_paid_phase_zero_seed": reused_phase_zero,
            "nfev_connector": connector["nfev_connector"],
            "elapsed_seconds": time.monotonic() - started})
        return item

    low, high = evaluate(0.0), evaluate(2 * np.pi)
    f0, f1 = low["connector"]["C_core_over_norm"], high["connector"]["C_core_over_norm"]
    if f0 * f1 > 0:
        raise ArithmeticError("numerical endpoints did not exhibit the proved phase sign reversal")
    root, info = brentq(lambda phase: evaluate(phase)["connector"]["C_core_over_norm"],
                       0.0, 2 * np.pi, xtol=args.phase_xtol,
                       rtol=4 * np.finfo(float).eps, full_output=True)
    selected = evaluate(root)
    derivative_rows = []
    for h in (args.phase_derivative_step, args.phase_derivative_step / 2):
        left, right = evaluate(root - h), evaluate(root + h)
        derivative_rows.append({
            "step": h,
            "d_C_over_norm_d_phase": (right["connector"]["C_core_over_norm"] - left["connector"]["C_core_over_norm"]) / (2 * h),
            "d_C_over_A_d_phase": (right["connector"]["C_core_over_A"] - left["connector"]["C_core_over_A"]) / (2 * h),
        })
    tighter = evaluate(root, rtol=fine_rtol / args.tolerance_refinement,
                       atol=fine_atol / args.tolerance_refinement)
    laterM = evaluate(root, M=args.M + 1, rtol=fine_rtol / args.tolerance_refinement,
                      atol=fine_atol / args.tolerance_refinement)
    selected_summary = seed_summary(selected["seed"], tighter["seed"], laterM["seed"])
    field_report = full_field_report(tighter, root, par, 2, args.connector_nodes)
    modes = []
    for j in (4, 6, 8):
        try:
            item = evaluate(root, j=j)
            modes.append({"mode": j, "status": "finite_probe_returned",
                          "A_core": item["connector"]["A_core"], "C_core": item["connector"]["C_core"],
                          "C_core_over_norm": item["connector"]["C_core_over_norm"],
                          "C_core_over_A": item["connector"]["C_core_over_A"],
                          "R571_does_not_certify_this_mode_or_a_tame_inverse": True})
        except Exception as error:
            modes.append({"mode": j, "status": "finite_probe_failed",
                          "type": type(error).__name__, "message": str(error)})
    final = {
        "definition": definition, "selected_phase": root,
        "root_iterations": int(info.iterations), "root_function_calls": int(info.function_calls),
        "C_core_over_A_at_selected_tighter": tighter["connector"]["C_core_over_A"],
        "core_residual_change_under_tolerance_refinement": tighter["connector"]["C_core_over_A"] - selected["connector"]["C_core_over_A"],
        "core_residual_change_under_M_plus_1": laterM["connector"]["C_core_over_A"] - tighter["connector"]["C_core_over_A"],
        "phase_derivative_observations": derivative_rows,
        "nonzero_phase_derivative_numerical_evidence": bool(
            abs(derivative_rows[-1]["d_C_over_A_d_phase"]) > 1e-4
            and abs(derivative_rows[-1]["d_C_over_A_d_phase"]
                    - derivative_rows[0]["d_C_over_A_d_phase"])
            <= .05 * abs(derivative_rows[-1]["d_C_over_A_d_phase"])),
        "selected_phase_seed_comparisons": selected_summary,
        "unit_core_field": field_report, "higher_mode_probes": modes,
        "total_seed_RHS_evaluations": int(nfev_seed), "total_connector_RHS_evaluations": int(nfev_connector),
        "counted_actual_RHS_calls_including_failed_finite_probes": RHS_COUNTS,
        "elapsed_seconds": time.monotonic() - started,
        "numerical_simple_zero_is_not_a_continuous_spectrum_or_nonlinear_theorem": True,
        "finite_amplitude_branch_constructed": False, "complete": False,
    }
    emit("R571_SHOOTING_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("R571_SHOOTING_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
