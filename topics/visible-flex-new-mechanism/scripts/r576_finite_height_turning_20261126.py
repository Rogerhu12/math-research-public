#!/usr/bin/env python3
"""R576 finite-height design with actual flat end modes and exact turning.

All scientific execution belongs to public Actions. This is static-metric
design, not fixed-g refinement. The exact mathematical tails are the infinite
DtN limits of R571/R583. Their finite ODE evaluation and all angular/radial
sampling remain observations, not continuous certificates.
"""
import argparse
from dataclasses import asdict, replace
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import BSpline
from scipy.optimize import brentq

SCHEMA = "r576-flat-seeded-finite-height-turning-v1"
HERE = Path(__file__).resolve().parent
SEED_FILE = "r571_milder_seed_outer_jets_20261126.py"
SEED_SHA = "ede50d8c4d362d77f9618b3481233d32e5ecc73842af7d84dddd8c78bb518970"
GAIN_FILE = "r571_nonmonotone_connector_gain_20261126.py"
GAIN_SHA = "81407b0e9a262d65d3037ccffa191ecdc501087911e3daf75edf0fe03cda8deb"
RC, R0, ELL = .22, .30, .2
MODES = (2, 4, 6, 8)
COUNTS = {"seed_RHS": 0, "connector_RHS": 0, "core_basis_RHS": 0,
          "height_RHS": 0, "height_quadrature_integrand": 0,
          "basis_points": 0, "geometry_calls": 0, "geometry_points": 0,
          "complex_step_columns": 0, "turning_bisections": 0,
          "linear_solves": 0, "line_search_trials": 0}

def emit(tag, value):
    print(tag + " " + json.dumps(value, sort_keys=True, separators=(",", ":"),
                                 allow_nan=False), flush=True)

def import_bound(name, filename, expected):
    path = HERE / filename
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected:
        raise RuntimeError("source identity mismatch: " + filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

seed = import_bound("r576_seed_source", SEED_FILE, SEED_SHA)
gain = import_bound("r576_gain_source", GAIN_FILE, GAIN_SHA)

def step2(x):
    x = np.asarray(x, dtype=float)
    value, first, second = np.zeros_like(x), np.zeros_like(x), np.zeros_like(x)
    value[x >= 1] = 1
    selected = (x > 0) & (x < 1)
    t = x[selected]
    s, ds = gain.step_and_first(t)
    ell1 = t ** -2 + (1 - t) ** -2
    ell2 = -2 * t ** -3 + 2 * (1 - t) ** -3
    value[selected] = s
    first[selected] = ds
    second[selected] = s * (1 - s) * ((1 - 2 * s) * ell1 ** 2 + ell2)
    return value, first, second

CORE_ONSET_FRACTION = .1

def radial_slope(par, r):
    """Same finite part; make the t**1.1 core onset genuinely C-infinity."""
    r = np.asarray(r, dtype=float)
    value, first = gain.finite_slope(par, r)
    value, first = np.asarray(value).copy(), np.asarray(first).copy()
    active = r > par.core_start
    t = (r[active] - par.core_start) / (par.R - par.core_start)
    raw = par.core_scale * t ** par.beta / (1 - t * t) ** par.alpha
    raw_r = raw / (par.R - par.core_start) * (par.beta / t + 2 * par.alpha * t / (1 - t * t))
    chi, chir, _ = step2(t / CORE_ONSET_FRACTION)
    chir /= CORE_ONSET_FRACTION * (par.R - par.core_start)
    value[active] += chi * raw
    first[active] += chi * raw_r + chir * raw
    return value, first

def spatial_jets(par, x):
    """Regular x jets of the same smoothed background, including x=0."""
    x = np.asarray(x, dtype=float)
    a, ax, axx, old_zx, old_zxx = gain.spatial_jets(par, x)
    wf, wfr = gain.finite_slope(par, a)
    raw_core = old_zx + ax * wf
    raw_core_x = old_zxx + axx * wf + ax * ax * wfr
    gamma = par.radial_width / (par.R - par.core_start)
    t = 1 - gamma * x ** par.m
    chi, chit, _ = step2(t / CORE_ONSET_FRACTION)
    chi_x = chit / CORE_ONSET_FRACTION * (-gamma * par.m * x ** (par.m - 1))
    zx = chi * raw_core - ax * wf
    zxx = chi * raw_core_x + chi_x * raw_core - axx * wf - ax * ax * wfr
    return a, ax, axx, zx, zxx

def scaled_values(values, logarithm):
    values = np.asarray(values)
    nonzero = values != 0
    result = np.zeros_like(values)
    exponents = np.log(np.abs(values[nonzero])) + logarithm
    if np.any(exponents > np.log(np.finfo(float).max)):
        raise ArithmeticError("seed display scale overflow")
    with np.errstate(under="ignore"):
        result[nonzero] = np.sign(values[nonzero]) * np.exp(exponents)
    return result

class FlatSeed:
    """Dense evaluation of the declared finite approximation to one true germ."""
    def __init__(self, mode, args):
        self.mode, self.args = mode, args
        seed.ANGULAR_MODE, seed.PHASE = mode, 0.0
        inner = seed.inner_slope(args.M, args.rtol, args.atol, .1)
        COUNTS["seed_RHS"] += inner["nfev_inner"]
        self.inner = inner
        self.alpha = inner["alpha_first"]
        self.minimum_radius = RC + ELL / self.alpha
        last_u = ELL / (R0 - RC)
        centers = np.pi / 2 + 2 * np.pi * np.arange(seed.FIRST_PEAK + 1)
        breaks = np.r_[self.alpha,
                       np.sort(centers[(centers < self.alpha) & (centers > last_u)])[::-1],
                       last_u]
        state = np.array([1.0, inner["z_at_alpha_first"]])
        log_scale = 0.0
        self.segments = []
        for high, low in zip(breaks[:-1], breaks[1:]):
            sol = seed.integrate(float(high), float(low), state,
                                 args.rtol, args.atol, .1, dense=True)
            COUNTS["seed_RHS"] += int(sol.nfev)
            self.segments.append((float(low), float(high), sol.sol, log_scale))
            outgoing = sol.y[:, -1]
            scale = float(np.max(np.abs(outgoing)))
            if not (scale > 0 and np.isfinite(scale)):
                raise ArithmeticError("seed normalization failed")
            log_scale += math.log(scale)
            state = outgoing / scale
        outer = seed.scaled_jets(last_u, state)
        if mode == 2:
            self.display_log = gain.SOURCE["common_display_log_scale"]
        else:
            self.display_log = log_scale + math.log(math.hypot(outer[0], .08 * outer[1]))
        self.outer = scaled_values(outer, log_scale - self.display_log)
        self.finite_inner_data = {
            "mode": mode, "M": args.M, "terminal_peak_index": args.M + 1,
            "alpha_first": self.alpha, "z_alpha_first": inner["z_at_alpha_first"],
            "rho_first_plus_one": inner["rho_first_plus_one"],
            "display_log_scale": self.display_log,
            "minimum_numerically_evaluated_radius": self.minimum_radius,
            "exact_model_below_this_radius": "the infinite DtN flat germ, not a frozen interval",
            "finite_tail_and_ODE_error_are_not_certified_here": True,
            "outer_jets": self.outer.tolist(),
        }

    def evaluate(self, r):
        r = np.asarray(r, dtype=float)
        if np.any(r < self.minimum_radius * (1 - 1e-14)) or np.any(r > R0 * (1 + 1e-14)):
            raise ValueError("requested seed node outside declared numerical window")
        seed.ANGULAR_MODE, seed.PHASE = self.mode, 0.0
        u = ELL / (r - RC)
        answer = np.zeros((r.size, 13))
        assigned = np.zeros(r.size, dtype=bool)
        for low, high, dense, logarithm in self.segments:
            selected = (~assigned) & (u >= low - 1e-12) & (u <= high + 1e-12)
            for index in np.flatnonzero(selected):
                jets = seed.scaled_jets(float(u[index]), dense(float(u[index])))
                answer[index] = scaled_values(jets, logarithm - self.display_log)
                assigned[index] = True
        if not np.all(assigned):
            raise ArithmeticError("unassigned seed evaluation node")
        return answer[:, :3]

class AdmissibleMode:
    """True inner germ plus an explicit core-trace correction in the residual."""
    def __init__(self, flat, profile, args, *, build_basis=True):
        self.flat, self.par, self.args = flat, profile, args
        self.mode, self.mu = flat.mode, flat.mode ** 2
        w0 = float(radial_slope(profile, R0)[0])
        A0, C0 = flat.outer[4], flat.outer[0]

        def rhs(r, y):
            COUNTS["connector_RHS"] += 1
            w, wr = (float(v) for v in radial_slope(profile, r))
            A, D = y
            return [(A - self.mu * D) / r, -wr / w * (A - D)]

        self.forward = solve_ivp(rhs, (R0, profile.switch_radius),
                                 [A0, A0 - w0 * C0], method="DOP853",
                                 rtol=args.rtol, atol=args.atol,
                                 max_step=.003, dense_output=True)
        if not self.forward.success:
            raise ArithmeticError(self.forward.message)
        wsw = float(radial_slope(profile, profile.switch_radius)[0])
        Asw, Dsw = self.forward.y[:, -1]
        initial = [Asw, (Asw - Dsw) / wsw]
        self.xsw = float(profile.x_of_r(profile.switch_radius))

        def rhs_x(x, y):
            COUNTS["core_basis_RHS"] += 1
            a, ax, _, zx, _ = (float(v) for v in spatial_jets(profile, x))
            A, C = y.reshape(2, -1)
            Ax = -(self.mu - 1) * ax / a * A - self.mu * zx / a * C
            Cx = -ax / zx * Ax
            return np.r_[Ax, Cx]

        self.raw_core = solve_ivp(rhs_x, (self.xsw, 0), initial, method="DOP853",
                                  rtol=args.rtol, atol=args.atol,
                                  max_step=.006, dense_output=True)
        if not self.raw_core.success:
            raise ArithmeticError(self.raw_core.message)
        self.Acore, self.Ccore = (float(v) for v in self.raw_core.y[:, -1])
        if not build_basis:
            return
        if abs(self.Acore) <= 1e-14 * math.hypot(self.Acore, self.Ccore):
            raise ArithmeticError("core A normalization too small")
        self.cut_left, self.cut_right = .55, .65
        xleft = float(profile.x_of_r(self.cut_left))
        self.core_pair = solve_ivp(rhs_x, (0, xleft), [1., 0., 0., 1.],
                                   method="DOP853", rtol=args.rtol, atol=args.atol,
                                   max_step=.004, dense_output=True)
        if not self.core_pair.success:
            raise ArithmeticError(self.core_pair.message)
        pair_switch = self.core_pair.sol(self.xsw).reshape(2, 2)
        recombined = pair_switch @ np.array([self.Acore, self.Ccore])
        self.match_observation = (recombined - np.asarray(initial)).tolist()

    def AC_jets(self, r, A, C):
        w, wr = radial_slope(self.par, r)
        Cr = self.mu * C / r - (self.mu - 1) * A / (r * w)
        Crr = (self.mu - 1) * wr * A / (r * w * w)
        return np.stack([C, Cr, Crr], axis=1)

    def evaluate(self, r):
        r = np.asarray(r, dtype=float)
        COUNTS["basis_points"] += int(r.size)
        result = np.zeros((r.size, 3))
        tail = r <= R0
        if np.any(tail):
            result[tail] = self.flat.evaluate(r[tail]) / self.Acore
        body = (r > R0) & (r < self.cut_right)
        if np.any(body):
            rb = r[body]
            A, D = self.forward.sol(rb)
            w = radial_slope(self.par, rb)[0]
            C = (A - D) / w
            values = self.AC_jets(rb, A, C) / self.Acore
            active = rb > self.cut_left
            if np.any(active):
                ra = rb[active]
                pair = self.core_pair.sol(self.par.x_of_r(ra)).reshape(2, 2, -1)
                admissible = self.AC_jets(ra, pair[0, 0], pair[1, 0])
                raw = values[active].copy()
                chi, chir, chirr = step2((ra - self.cut_left) / (self.cut_right - self.cut_left))
                chir /= self.cut_right - self.cut_left
                chirr /= (self.cut_right - self.cut_left) ** 2
                delta = admissible - raw
                values[active, 0] += chi * delta[:, 0]
                values[active, 1] += chi * delta[:, 1] + chir * delta[:, 0]
                values[active, 2] += chi * delta[:, 2] + 2 * chir * delta[:, 1] + chirr * delta[:, 0]
            result[body] = values
        core = r >= self.cut_right
        if np.any(core):
            rr = r[core]
            pair = self.core_pair.sol(self.par.x_of_r(rr)).reshape(2, 2, -1)
            result[core] = self.AC_jets(rr, pair[0, 0], pair[1, 0])
        return result

    def receipt(self):
        return {"mode": self.mode, "raw_A_core": self.Acore,
                "raw_C_core": self.Ccore, "raw_C_over_A": self.Ccore / self.Acore,
                "core_trace_correction_support": [self.cut_left, self.cut_right],
                "core_correction_is_in_complete_height_residual": True,
                "core_pair_transfer_match_observation": self.match_observation,
                "corrected_core_C": 0.,
                "corrected_core_W_f_r": -(self.mu - 1) / self.par.R}

def select_resonant_background(flat, reference_profile, args):
    """New shooting for the newly smoothed onset; the old H is only a reference."""
    cache = {}
    def evaluate(H):
        key = float(H)
        if key not in cache:
            profile = replace(reference_profile, gain_height=key)
            transfer = AdmissibleMode(flat, profile, args, build_basis=False)
            norm = math.hypot(transfer.Acore, transfer.Ccore)
            if not norm > 0:
                raise ArithmeticError("nonzero shooting field lost")
            cache[key] = (transfer.Ccore / norm, transfer.Acore, transfer.Ccore)
        return cache[key][0]
    heights = np.geomspace(.02, 4., 33)
    values = [evaluate(float(H)) for H in heights]
    brackets = [(float(a), float(b)) for a, b, fa, fb in
                zip(heights[:-1], heights[1:], values[:-1], values[1:]) if fa * fb < 0]
    exact_samples = [float(H) for H, value in zip(heights, values) if value == 0]
    emit("HEIGHT_NEW_BACKGROUND_SHOOTING", {
        "core_onset_flat_factor": "S(t/.1), t=(r-.55)/(.85-.55)",
        "old_H_is_only_a_reference": reference_profile.gain_height,
        "scan_heights": heights.tolist(), "scan_values_C_over_norm": values,
        "brackets": brackets, "exact_zero_samples": exact_samples})
    if exact_samples:
        Hstar = min(exact_samples, key=lambda H: abs(H - reference_profile.gain_height))
    elif brackets:
        a, b = min(brackets, key=lambda ab: abs((ab[0] + ab[1]) / 2 - reference_profile.gain_height))
        Hstar = float(brentq(evaluate, a, b, xtol=2e-11, rtol=1e-12))
    else:
        raise ArithmeticError("declared new smooth-onset H scan has no shooting bracket")
    evaluate(Hstar)
    value, Ac, Cc = cache[Hstar]
    emit("HEIGHT_NEW_BACKGROUND_ROOT", {"gain_height": Hstar, "Acore": Ac,
         "Ccore": Cc, "C_over_A": Cc / Ac, "C_over_norm": value,
         "actual_distinct_transfers": len(cache), "root_is_a_numerical_observation": True})
    return replace(reference_profile, gain_height=Hstar)

def radial_nodes(minimum, R, density):
    umax = ELL / (minimum - RC)
    uniform = np.linspace(2.5, umax, 128 * density + 1)
    features = []
    for n in range(18):
        for center in (np.pi / 2 + 2 * np.pi * n, 3 * np.pi / 2 + 2 * np.pi * n):
            for offset in (-2., -1., 0., 1., 2.):
                value = center + offset / math.sqrt(max(center, 1.0))
                if 2.5 <= value <= umax:
                    features.append(value)
    tail = RC + ELL / np.r_[uniform, features]
    body = np.linspace(R0, R - .03, 64 * density + 1)
    core = R - np.geomspace(1e-7, .03, 32 * density + 1)
    return np.unique(np.r_[tail, body, core, .34, .37, .48, .55, .61, .65])

class DomainError(Exception):
    pass

class HeightDesign:
    def __init__(self, profile, modes, knots, args):
        self.par, self.modes, self.args = profile, modes, args
        self.minimum = max(v.flat.minimum_radius for v in modes)
        self.nb = len(knots) + 6
        t = np.r_[np.repeat(RC, 6), knots, np.repeat(profile.R, 6)]
        self.bs = BSpline(t, np.eye(self.nb), 5, extrapolate=False)
        self.nq = 1 + len(MODES) - 1 + len(MODES) * self.nb
        self.cache = {}
        normal_nodes = radial_nodes(self.minimum * (1 + 1e-12), profile.R, 1)
        all_values = np.stack([m.evaluate(normal_nodes) for m in modes], axis=1)
        self.mode_height_scales = np.maximum(1e-100, np.max(np.abs(all_values[:, :, 0]), axis=0))
        self.envelope_scale = 1.0
        raw_envelope = self.envelope(normal_nodes, all_values)
        self.envelope_scale = float(np.max(raw_envelope[:, 0]))
        if not self.envelope_scale > 0:
            raise ArithmeticError("free height envelope vanished")
        xmax = float(profile.x_of_r(self.minimum))

        def h_rhs(x, y):
            COUNTS["height_RHS"] += 1
            return [float(spatial_jets(profile, x)[3])]

        self.h_integral = solve_ivp(h_rhs, (0, xmax), [0.], method="DOP853",
                                    rtol=args.rtol, atol=args.atol,
                                    max_step=.002, dense_output=True)
        if not self.h_integral.success:
            raise ArithmeticError(self.h_integral.message)

    def envelope(self, r, fields):
        sf = fields / self.mode_height_scales[None, :, None]
        a = np.sum(sf[:, :, 0] ** 2, axis=1)
        ar = 2 * np.sum(sf[:, :, 0] * sf[:, :, 1], axis=1)
        arr = 2 * np.sum(sf[:, :, 1] ** 2 + sf[:, :, 0] * sf[:, :, 2], axis=1)
        # Positive throughout the open tail, faster flat than the genuine modes.
        t, d, power, kappa = r - RC, self.par.R - r, 2 + 2 * self.par.alpha, 1e-4
        logarithm = -kappa / t ** 4 + power * np.log(d)
        with np.errstate(under="ignore"):
            g = np.exp(logarithm)
        l1, l2 = 4 * kappa / t ** 5 - power / d, -20 * kappa / t ** 6 - power / d ** 2
        return np.stack([a + g, ar + g * l1, arr + g * (l1 * l1 + l2)], axis=1) / self.envelope_scale

    def prepare(self, r, ntheta):
        r = np.asarray(r, dtype=float)
        key = (r.tobytes(), int(ntheta))
        if key in self.cache:
            return self.cache[key]
        fields = np.stack([m.evaluate(r) for m in self.modes], axis=1)
        env = self.envelope(r, fields)
        B, Br, Brr = (self.bs(r, nu=k) for k in range(3))
        bulk = np.stack([env[:, 0, None] * B,
                         env[:, 1, None] * B + env[:, 0, None] * Br,
                         env[:, 2, None] * B + 2 * env[:, 1, None] * Br + env[:, 0, None] * Brr], axis=2)
        theta = 2 * np.pi * np.arange(ntheta) / ntheta
        modes = np.asarray(MODES)
        co, si = np.cos(modes[:, None] * theta), np.sin(modes[:, None] * theta)
        difference = theta[:, None] - theta[None, :]
        primitive = np.zeros_like(difference)
        derivative = np.zeros_like(difference)
        second_derivative = np.zeros_like(difference)
        for k in range(1, ntheta // 2):
            primitive += (2 / ntheta) * np.sin(k * difference) / k
            derivative -= (2 / ntheta) * k * np.sin(k * difference)
            second_derivative -= (2 / ntheta) * k * k * np.cos(k * difference)
        second_derivative -= (ntheta // 2) ** 2 / ntheta * np.cos((ntheta // 2) * difference)
        # A real linear primitive matrix preserves complex-step derivatives.
        w0, wr0 = radial_slope(self.par, r)
        alternate = replace(self.par, gain_height=self.par.gain_height + 1.)
        w1, wr1 = radial_slope(alternate, r)
        gain_w, gain_wr = w1 - w0, wr1 - wr0
        h0 = self.par.core_height + self.h_integral.sol(self.par.x_of_r(r))[0]

        def gain_integrand(t):
            COUNTS["height_quadrature_integrand"] += 1
            left = gain.step_and_first(np.asarray((t - self.par.gain_start) /
                                      (self.par.gain_peak - self.par.gain_start)))[0]
            right = gain.step_and_first(np.asarray((self.par.gain_end - t) /
                                       (self.par.gain_end - self.par.gain_peak)))[0]
            return float(left * right)

        total_gain = quad(gain_integrand, self.par.gain_start, self.par.gain_end,
                          epsabs=1e-13, epsrel=1e-12, points=[self.par.gain_peak])[0]
        hg = np.zeros_like(r)
        hg[r <= self.par.gain_start] = total_gain
        for index in np.flatnonzero((r > self.par.gain_start) & (r < self.par.gain_end)):
            points = [self.par.gain_peak] if r[index] < self.par.gain_peak else None
            hg[index] = quad(gain_integrand, float(r[index]), self.par.gain_end,
                             epsabs=1e-13, epsrel=1e-12, points=points)[0]
        data = {"r": r, "theta": theta, "fields": fields, "bulk": bulk,
                "cos": co, "sin": si, "primitive": primitive,
                "derivative": derivative, "second_derivative": second_derivative,
                "w0": w0, "wr0": wr0, "gain_w": gain_w, "gain_wr": gain_wr,
                "h0": h0, "gain_height": hg}
        self.cache[key] = data
        return data

    def height_jets(self, q, amplitude, data):
        coefficients = np.r_[np.ones(1, dtype=q.dtype), q[1:len(MODES)]]
        coefficients = coefficients * amplitude
        bulk_coefficients = amplitude * q[len(MODES):].reshape(len(MODES), self.nb)
        radial = data["fields"] * coefficients[None, :, None]
        radial += np.einsum("rbk,jb->rjk", data["bulk"], bulk_coefficients)
        co, si, mu, j = data["cos"], data["sin"], np.asarray(MODES) ** 2, np.asarray(MODES)
        v = radial[:, :, 0] @ co
        vr, vrr = radial[:, :, 1] @ co, radial[:, :, 2] @ co
        vt = -(radial[:, :, 0] * j) @ si
        vtt = -(radial[:, :, 0] * mu) @ co
        vrt = -(radial[:, :, 1] * j) @ si
        scale = self.args.height_saturation
        th = np.tanh(v / scale)
        d1 = 1 - th * th
        d2 = -2 * th * d1 / scale
        f = scale * th
        fr, frr = d1 * vr, d1 * vrr + d2 * vr * vr
        f -= np.mean(f, axis=1, keepdims=True)
        fr -= np.mean(fr, axis=1, keepdims=True)
        frr -= np.mean(frr, axis=1, keepdims=True)
        ft = d1 * vt
        ftt = d1 * vtt + d2 * vt * vt
        frt = d1 * vrt + d2 * vr * vt
        return f, fr, frr, ft, ftt, frt

    def geometry(self, q, amplitude, data, *, details=False):
        COUNTS["geometry_calls"] += 1
        COUNTS["geometry_points"] += int(data["r"].size * data["theta"].size)
        r = data["r"][:, None]
        f, fr, frr, ft, ftt, frt = self.height_jets(q, amplitude, data)
        hdelta = q[0] - self.par.gain_height
        w = (data["w0"] + hdelta * data["gain_w"])[:, None]
        wr = (data["wr0"] + hdelta * data["gain_wr"])[:, None]
        p = -w + fr
        b2 = r * r - ft * ft
        if np.min(np.real(b2 / (r * r))) <= .05:
            raise DomainError("angular graph speed lost its positive margin")
        b = np.sqrt(b2)
        N = r / b + r * r * p * ftt / b ** 3
        if np.min(np.real(N)) <= 1e-8:
            raise DomainError("positive-turning numerator lost its margin")
        shift = -2 * w * fr + fr * fr + p * p * ft * ft / b2
        reference = np.max(np.real(shift), axis=1, keepdims=True)
        gap = reference - np.real(shift)
        left = np.zeros_like(reference)
        right = np.mean(np.real(N), axis=1, keepdims=True) ** 2 + 1.
        for _ in range(56):
            middle = (left + right) / 2
            value = np.mean(np.real(N) / np.sqrt(middle + gap), axis=1, keepdims=True)
            choose_left = value > 1
            left = np.where(choose_left, middle, left)
            right = np.where(choose_left, right, middle)
        COUNTS["turning_bisections"] += 56 * int(r.size)
        lam = ((left + right) / 2).astype(np.result_type(q, float))
        for _ in range(3):
            u2 = lam + reference - shift
            if not np.all(np.isfinite(u2)) or np.min(np.real(u2)) <= 0:
                raise DomainError("implicit turning root lost positivity")
            u = np.sqrt(u2)
            turn = np.mean(N / u, axis=1, keepdims=True)
            den = np.mean(N / u ** 3, axis=1, keepdims=True)
            lam += 2 * (turn - 1) / den
        u2, e = lam + reference - shift, lam + reference
        if np.min(np.real(u2)) <= 1e-12:
            raise DomainError("outward graph velocity lost its positive margin")
        u = np.sqrt(u2)
        E = w * w + e
        a = N / u
        M = b ** 3 * N / (r * r)
        across = frt - ft / r
        At = (-r * w * frr - r * wr * fr - e * wr * ftt
              + E * frr * ftt - w * wr * fr * ftt - E * across * across
              + r * fr * frr + w * wr * ft * ft / r)
        weight = r * r / (u ** 3 * b ** 3)
        er = 2 * np.mean(weight * At, axis=1, keepdims=True) / np.mean(N / u ** 3, axis=1, keepdims=True)
        residual = weight * (At - er * M / 2)
        primitive = data["primitive"]
        pi = lambda values: values @ primitive.T
        psi = data["theta"][None, :] + np.pi / 2 + pi(a - 1)
        Tx, Ty = np.cos(psi), np.sin(psi)
        JT = np.stack([-Ty, Tx], axis=2)
        T = np.stack([Tx, Ty], axis=2)
        pir = pi(residual)
        Wstar = np.stack([pi(b * pir * JT[:, :, k]) for k in range(2)], axis=2)
        v = -p * ft / b
        pred = v[:, :, None] * T - u[:, :, None] * JT
        Yr = pred + Wstar
        outward = -np.sum(Yr * JT, axis=2)
        if np.min(np.real(outward / u)) <= .05:
            raise DomainError("identity-predicted outward direction lost its margin")
        residual_vector = (Wstar / np.sqrt(E)[:, :, None]).ravel() / amplitude
        if not details:
            return residual_vector
        Y = np.stack([pi(b * T[:, :, k]) for k in range(2)], axis=2)
        Yt = b[:, :, None] * T
        br = (r - ft * frt) / b
        Vt = 2 * r * r * p * frt / b2 + 2 * r * r * p * p * ft * ftt / b2 ** 2
        ut = -Vt / (2 * u)
        c = (v * a - ut) / b
        psir = c + pir
        Yrt = br[:, :, None] * T + (b * psir)[:, :, None] * JT
        bt = -ft * ftt / b
        Ytt = bt[:, :, None] * T + (b * a)[:, :, None] * JT
        deltaE = 2 * np.sum(Wstar * pred, axis=2) + np.sum(Wstar * Wstar, axis=2)
        Factual = b * np.sum(Wstar * T, axis=2)
        ec, fc = deltaE / E, Factual / (r * np.sqrt(E))
        eta = (np.abs(np.real(ec)) + np.sqrt(np.real(ec) ** 2 + 4 * np.real(fc) ** 2)) / 2
        Z = data["h0"][:, None] + hdelta * data["gain_height"][:, None] + f
        return {"residual_vector": residual_vector, "Y": Y, "Yr": Yr, "Yt": Yt,
                "Yrt": Yrt, "Ytt": Ytt, "Z": Z, "p": p, "q": ft,
                "Zrr": -wr + frr, "Zrt": frt, "Ztt": ftt,
                "E": E, "e": e, "er": er, "u": u, "b": b, "N": N,
                "R": residual, "Wstar": Wstar, "eta": eta,
                "turning_error": np.mean(a, axis=1) - 1,
                "closure_error": np.mean(b[:, :, None] * T, axis=1),
                "identity_outward_ratio": outward / u}

def small_report(model, q, amplitude, data):
    g = model.geometry(q, amplitude, data, details=True)
    where = np.unravel_index(int(np.argmax(g["eta"])), g["eta"].shape)
    return {"amplitude": amplitude, "gain_height": float(q[0]),
            "eta_max": float(np.max(g["eta"])),
            "eta_attainer": [float(data["r"][where[0]]), float(data["theta"][where[1]])],
            "b_over_r_min": float(np.min(g["b"] / data["r"][:, None])),
            "N_min": float(np.min(g["N"])), "u_min": float(np.min(g["u"])),
            "identity_outward_ratio_min": float(np.min(g["identity_outward_ratio"])),
            "turning_error_max": float(np.max(np.abs(g["turning_error"]))),
            "angular_closure_error_max": float(np.max(np.abs(g["closure_error"]))),
            "Darboux_R_max": float(np.max(np.abs(g["R"]))),
            "sampled_ball_max": float(np.max(np.sqrt(np.sum(g["Y"] ** 2, axis=2) + g["Z"] ** 2))),
            "sampled_height_min": float(np.min(g["Z"])),
            "sampled_abs_y_max": float(np.max(np.abs(g["Y"][:, :, 1]))),
            "r_nodes": int(data["r"].size), "theta_nodes": int(data["theta"].size)}

def actual_curvature_observation(model, q, amplitude, r, ntheta, factor=1.0):
    """Differentiate the reconstructed position itself, including spectral alias."""
    data = model.prepare(r, ntheta)
    g = model.geometry(q, amplitude, data, details=True)
    step = factor * np.minimum(1e-6, .002 * np.minimum(r - model.minimum, model.par.R - r))
    if np.any(step <= 0):
        raise ValueError("curvature probe needs strictly interior numerical nodes")
    plus = model.geometry(q, amplitude, model.prepare(r + step, ntheta), details=True)
    minus = model.geometry(q, amplitude, model.prepare(r - step, ntheta), details=True)
    Yr = (plus["Y"] - minus["Y"]) / (2 * step[:, None, None])
    Yrr = (plus["Y"] - 2 * g["Y"] + minus["Y"]) / step[:, None, None] ** 2
    Yt = np.stack([g["Y"][:, :, k] @ data["derivative"].T for k in range(2)], axis=2)
    Yrt = np.stack([Yr[:, :, k] @ data["derivative"].T for k in range(2)], axis=2)
    Ytt = np.stack([g["Y"][:, :, k] @ data["second_derivative"].T for k in range(2)], axis=2)
    Xr = np.concatenate([Yr, g["p"][:, :, None]], axis=2)
    Xt = np.concatenate([Yt, g["q"][:, :, None]], axis=2)
    Xrr = np.concatenate([Yrr, g["Zrr"][:, :, None]], axis=2)
    Xrt = np.concatenate([Yrt, g["Zrt"][:, :, None]], axis=2)
    Xtt = np.concatenate([Ytt, g["Ztt"][:, :, None]], axis=2)
    normal = np.cross(Xr, Xt)
    normal /= np.linalg.norm(normal, axis=2)[:, :, None]
    E = np.sum(Xr * Xr, axis=2)
    F = np.sum(Xr * Xt, axis=2)
    G = np.sum(Xt * Xt, axis=2)
    l, m, n = (np.sum(normal * second, axis=2) for second in (Xrr, Xrt, Xtt))
    det = E * G - F * F
    twiceH = (l * G - 2 * m * F + n * E) / det
    K = (l * n - m * m) / det
    disc = np.maximum(0., twiceH * twiceH - 4 * K)
    kp, km = (twiceH + np.sqrt(disc)) / 2, (twiceH - np.sqrt(disc)) / 2
    kabs = np.maximum(np.abs(kp), np.abs(km))
    index = np.unravel_index(int(np.argmax(kabs)), kabs.shape)
    model_T = g["Yt"] / g["b"][:, :, None]
    model_JT = np.stack([-model_T[:, :, 1], model_T[:, :, 0]], axis=2)
    direct_outward_ratio = -np.sum(Yr * model_JT, axis=2) / g["u"]
    rr = r[:, None]
    ec, fc, gc = E / g["E"] - 1, F / (rr * np.sqrt(g["E"])), G / (rr * rr) - 1
    direct_eta = (np.abs(ec + gc) + np.sqrt((ec - gc) ** 2 + 4 * fc * fc)) / 2
    ei = np.unravel_index(int(np.argmax(direct_eta)), direct_eta.shape)
    return {"absolute_curvature_max": float(kabs[index]),
            "curvature_attainer_r_theta": [float(r[index[0]]), float(data["theta"][index[1]])],
            "direct_reconstructed_metric_eta": float(direct_eta[ei]),
            "metric_attainer_r_theta": [float(r[ei[0]]), float(data["theta"][ei[1]])],
            "identity_metric_eta_on_same_nodes": float(np.max(g["eta"])),
            "Yr_identity_vs_position_difference": float(np.max(np.abs(Yr - g["Yr"]))),
            "angular_G_relative_defect": float(np.max(np.abs(gc))),
            "direct_position_outward_ratio_min": float(np.min(direct_outward_ratio)),
            "finite_radial_difference_factor": factor,
            "r_nodes": int(r.size), "theta_nodes": int(ntheta),
            "planar_position_differentiated_height_analytic_jets": True,
            "continuous_or_interval_curvature_certificate": False}

def jacobian(model, q, amplitude, data):
    columns = []
    for k in range(q.size):
        z = q.astype(complex)
        z[k] += 1e-25j
        columns.append(np.imag(model.geometry(z, amplitude, data)) / 1e-25)
        COUNTS["complex_step_columns"] += 1
    return np.stack(columns, axis=1)

def solve_stage(model, initial, amplitude, data, args, started):
    q = initial.copy()
    history = []
    damping = 1e-5
    status = "iteration_limit"
    for iteration in range(args.iterations):
        if time.monotonic() - started > args.maximum_seconds:
            status = "declared_run_budget"
            break
        try:
            residual = model.geometry(q, amplitude, data)
        except DomainError as error:
            status = "initial_domain_failure: " + str(error)
            break
        if not np.all(np.isfinite(residual)):
            status = "nonfinite_residual"
            break
        objective = float(np.dot(residual, residual) / residual.size)
        report = small_report(model, q, amplitude, data)
        report.update({"iteration": iteration, "objective": objective, "damping": damping})
        history.append(report)
        emit("HEIGHT_ITERATION", report)
        if report["eta_max"] <= args.target_eta:
            status = "sampled_metric_target"
            break
        J = jacobian(model, q, amplitude, data)
        if not np.all(np.isfinite(J)):
            status = "nonfinite_jacobian"
            break
        column_scale = np.maximum(np.linalg.norm(J, axis=0), 1e-12)
        Js = J / column_scale
        accepted = False
        for trial in range(6):
            COUNTS["linear_solves"] += 1
            normal = Js.T @ Js + damping * np.eye(q.size)
            scaled_step = np.linalg.solve(normal, -Js.T @ residual)
            direction = scaled_step / column_scale
            length = np.linalg.norm(direction)
            if length > 4:
                direction *= 4 / length
            for fraction in (1., .5, .25, .125, .0625, .03125, .015625):
                COUNTS["line_search_trials"] += 1
                proposed = q + fraction * direction
                if not (.02 <= proposed[0] <= 4):
                    continue
                try:
                    new_residual = model.geometry(proposed, amplitude, data)
                    if not np.all(np.isfinite(new_residual)):
                        continue
                    new_objective = float(np.dot(new_residual, new_residual) / new_residual.size)
                except DomainError:
                    continue
                if new_objective < objective * (1 - 1e-4 * fraction):
                    q = proposed
                    damping = max(1e-12, damping / 3)
                    accepted = True
                    break
            if accepted:
                break
            damping = min(1e10, damping * 10)
        if not accepted:
            status = "no_domain_preserving_descent"
            break
    return q, status, history

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-seconds", type=float, default=2400)
    parser.add_argument("--M", type=int, default=25)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--iterations", type=int, default=30)
    parser.add_argument("--theta-nodes", type=int, default=64)
    parser.add_argument("--target-eta", type=float, default=2e-9)
    parser.add_argument("--height-saturation", type=float, default=.15)
    parser.add_argument("--core-scale", type=float, default=.5)
    parser.add_argument("--initial-gain-height", type=float, default=.523503932624032)
    args = parser.parse_args()
    started = time.monotonic()
    profile = gain.Profile(R=.85, log_suppression=6., gain_height=args.initial_gain_height,
                           core_scale=args.core_scale)
    amplitudes = [1e-5, 3e-5, 1e-4, 3e-4, .001, .003, .01, .03, .1, .2]
    knots = [.235, .27, .34, .48, .64, .78]
    emit("HEIGHT_DEFINITION", {"schema": SCHEMA, "arguments": vars(args),
         "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "seed_source_sha256": SEED_SHA, "gain_source_sha256": GAIN_SHA,
         "reference_profile_before_new_shooting": asdict(profile),
         "core_onset_flat_factor": "S(t/.1), fixed; new identity",
         "modes": MODES, "radial_internal_knots": knots,
         "amplitude_sequence": amplitudes, "height_parameterization": "mean-zero hscale*tanh(v/hscale)",
         "core_mode2_W_f_r": "-3*amplitude/R",
         "higher_core_fluxes": "free through the actual corrected flat modes",
         "inner_tail_not_frozen": True, "same_metric_refinement": False,
         "complete_closed_family": False, "direct_reconstructed_metric_observation_tolerance": 8 * args.target_eta,
         "all_computation_this_public_workflow": True})
    flats = [FlatSeed(j, args) for j in MODES]
    for f in flats:
        emit("HEIGHT_FLAT_SEED", f.finite_inner_data)
    profile = select_resonant_background(flats[0], profile, args)
    emit("HEIGHT_SELECTED_PROFILE", asdict(profile))
    modes = [AdmissibleMode(f, profile, args) for f in flats]
    for m in modes:
        emit("HEIGHT_CORE_CORRECTION", m.receipt())
    model = HeightDesign(profile, modes, knots, args)
    active_density = 1
    r = radial_nodes(model.minimum * (1 + 1e-10), profile.R, active_density)
    data = model.prepare(r, args.theta_nodes)
    q = np.zeros(model.nq)
    q[0] = profile.gain_height
    amplitude = amplitudes[0]
    direction = np.sin(np.arange(model.nq) + .7)
    direction /= np.linalg.norm(direction)
    J = jacobian(model, q, amplitude, data)
    directional = J @ direction
    step = 2e-5
    central = (model.geometry(q + step * direction, amplitude, data)
               - model.geometry(q - step * direction, amplitude, data)) / (2 * step)
    err = np.linalg.norm(directional - central) / max(1e-30, np.linalg.norm(directional), np.linalg.norm(central))
    emit("HEIGHT_JACOBIAN_OBSERVATION", {"relative_direction_error": float(err),
         "central_step": step, "complex_step": 1e-25, "columns": model.nq})
    if not np.isfinite(err) or err > 2e-3:
        raise ArithmeticError("actual implicit-turning Jacobian direction check failed")
    stages = []
    for amplitude in amplitudes:
        exchange_history = []
        while True:
            q, status, history = solve_stage(model, q, amplitude, data, args, started)
            exchange = {"active_density": active_density, "status": status,
                        "iterations": len(history), "same_q_active": None, "same_q_fine": None}
            try:
                exchange["same_q_active"] = small_report(model, q, amplitude, data)
                fine_density = 2 * active_density
                fine_r = radial_nodes(model.minimum * (1 + 1e-10), profile.R, fine_density)
                fine_data = model.prepare(fine_r, fine_density * args.theta_nodes)
                exchange["same_q_fine"] = small_report(model, q, amplitude, fine_data)
                probe_r = fine_r[(fine_r > model.minimum + 1e-5) & (fine_r < profile.R - 1e-6)]
                exchange["direct_reconstruction_step"] = actual_curvature_observation(
                    model, q, amplitude, probe_r, fine_density * args.theta_nodes)
                exchange["direct_reconstruction_half_step"] = actual_curvature_observation(
                    model, q, amplitude, probe_r, fine_density * args.theta_nodes, .5)
            except DomainError as error:
                exchange["fine_domain_failure"] = str(error)
            exchange_history.append(exchange)
            emit("HEIGHT_GRID_EXCHANGE", exchange)
            fine_ok = (exchange["same_q_fine"] is not None
                       and exchange["same_q_fine"]["eta_max"] <= args.target_eta
                       and "direct_reconstruction_half_step" in exchange
                       and max(exchange["direct_reconstruction_step"]["direct_reconstructed_metric_eta"],
                               exchange["direct_reconstruction_half_step"]["direct_reconstructed_metric_eta"])
                           <= 8 * args.target_eta
                       and exchange["direct_reconstruction_step"]["direct_position_outward_ratio_min"] > 0
                       and exchange["direct_reconstruction_half_step"]["direct_position_outward_ratio_min"] > 0)
            if status != "sampled_metric_target" or fine_ok:
                break
            if active_density >= 2 or time.monotonic() - started > args.maximum_seconds:
                status = "fine_grid_target_unresolved"
                break
            active_density = fine_density
            data = fine_data
        record = {"amplitude": amplitude, "status": status, "coefficients": q.tolist(),
                  "grid_exchanges": exchange_history}
        stages.append(record)
        emit("HEIGHT_STAGE", record)
        if status != "sampled_metric_target":
            break
        if time.monotonic() - started > args.maximum_seconds:
            break
    emit("HEIGHT_FINAL", {"schema": SCHEMA, "elapsed_seconds": time.monotonic() - started,
         "counts": COUNTS, "imported_gain_counters": gain.COUNTS,
         "stages": stages, "mode_height_scales": model.mode_height_scales.tolist(),
         "free_envelope_scale": model.envelope_scale,
         "newly_regenerated_seed_profiles_are_for_this_nonlinear_basis_not_a_repeat_seed_conclusion": True,
         "uncomputed_inner_tail_nodes_are_not_claimed_as_certified": True,
         "same_metric_refinement": False, "continuous_reach_certificate": False,
         "complete_finite_isometric_family": False,
         "raw_arrays_tables_artifacts_releases_or_git_writes": False})

if __name__ == "__main__":
    main()
