#!/usr/bin/env python3
"""Actual-circle flat seed and undivided C2 core-return design.

New scientific identity. The 17 mean coordinates are the identified accepted
circle stage, not the zero-coefficient R569 background. Two compact controls
leave the actual tail and both open end collars unchanged. Scientific use is
restricted to the separately declared public Actions request. No finite
isometric family, fixed-metric refinement or continuous reach is asserted.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import BSpline
from scipy.optimize import brentq, minimize
from scipy.special import expit

REFERENCE_SOURCES = {
    "inverse_rotational_metric_20261126.py": "e25dff6a411e8edc485babe6545087cfbea2b6d16cd804e6dcb51f17d8fab319",
    "inverse_flat_oscillatory_tail_20261126.py": "b9c778fbeafb0d9beb061b3f472b8db1661daec5a78a63eb886a8e4770574f9b",
}
for filename, digest in REFERENCE_SOURCES.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != digest:
        raise RuntimeError("actual-circle source binding changed: " + filename)
import inverse_flat_oscillatory_tail_20261126 as physical

SCHEMA = "r582-actual-circle-flat-seed-undivided-return-with-compact-mean-controls-v1"
LENGTH, CORE_END, RC, ELL, AMP = .9, .036, .22, .2, .1
WIDTH, KAPPA, FIRST_PEAK = .864, 4.32, 160
TAIL_MOUTH = .82
CONTROL_LEFT, CONTROL_RIGHT = .06, .80
SOURCE_Q = np.r_[np.zeros(64), [
    -.35001924628214787, -.3531732092117735, -.3244617668413918,
    -.43706812962213554, -.5435744674362258, -.3821726524975292,
    -.5654097637847235, -.5041937321653266,
    0., -.0013474117462880936, -.09175492884312668,
    -.15680738719807807, -.05955223441757437, -.19856521037391323,
    -.5877276747743894, .09658185324267708, .6747017055797783]]
SOURCE = {
    "run_id": 45778418134, "job_id": 139767648038, "stage": 0,
    "source_commit": "668a3f6c6aee92b00c5ca547dd7677d257d0cdc0",
    "stage_JSON_bytes": 21505,
    "stage_JSON_sha256": "a78102463e4a816d00e000c969372af423a41ee93ab4996574b16048265b9324",
    "original_log_UTF8_bytes": 1042984,
    "original_log_UTF8_sha256": "7a1a626217d090742fed665049c96c4124a49b68d0d051c85fa6d305765f964d",
    "source_coordinates_are_not_reoptimized_here": True,
}
COUNTS = {"actual_weight_calls": 0, "inner_RHS": 0, "outer_RHS": 0,
          "background_grid_constructions": 0, "background_radial_points": 0,
          "linear_least_squares": 0, "mean_control_candidates": 0}


def emit(tag, data):
    print(tag + " " + json.dumps(data, sort_keys=True, separators=(",", ":"),
                                allow_nan=False), flush=True)


class ClockCheckpoint(RuntimeError):
    pass


class TailChartBoundary(RuntimeError):
    pass


class ActualTail:
    """R582's actual positive weight, with analytic u jets through order 3."""
    def __init__(self, q, deadline):
        self.q = np.asarray(q, dtype=float).copy()
        if self.q.shape != (81,) or np.any(self.q[:64] != 0):
            raise ValueError("the actual circular input needs 81 coordinates and zero angular coefficients")
        if np.max(abs(self.q[64:72])) > 1.5 or np.max(abs(self.q[72:80])) > 1:
            raise ValueError("input left the proved R582 mean-coordinate box")
        knots = np.r_[np.zeros(6), [1 / 3, 2 / 3], np.ones(6)]
        self.spline = BSpline(knots, np.eye(8), 5, extrapolate=False)
        self.deadline, self.maxima, self.last_completed = deadline, {}, None

    def check_clock(self):
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint("actual-circle cooperative scientific clock")

    def polynomial_jets(self, u, coefficients):
        s = LENGTH - ELL / np.sqrt(u)
        x = (s - CORE_END) / WIDTH
        jets = [float(self.spline(x, k) @ coefficients) / WIDTH ** k for k in range(4)]
        su, suu, suuu = .1 * u ** -1.5, -.15 * u ** -2.5, .375 * u ** -3.5
        p, ps, pss, psss = jets
        return np.array([p, ps * su, pss * su * su + ps * suu,
                         psss * su ** 3 + 3 * pss * su * suu + ps * suuu])

    def coefficients(self, u):
        self.check_clock()
        COUNTS["actual_weight_calls"] += 1
        u = float(u)
        if u < (ELL / (LENGTH - TAIL_MOUTH)) ** 2 * (1 - 1e-12):
            raise ValueError("actual R582 tail formula requested outside its exact background suffix")
        root = np.sqrt(u)
        t, x = 1 / (KAPPA * root), 1 - 1 / (KAPPA * root)
        lam = KAPPA * root - 1 / x
        lu = KAPPA / (2 * root) + t / (2 * u * x * x)
        luu = -KAPPA / (4 * u ** 1.5) - 3 * t / (4 * u * u * x * x) - t * t / (2 * u * u * x ** 3)
        luuu = (3 * KAPPA / (8 * u ** 2.5) + 15 * t / (8 * u ** 3 * x * x)
                 + 9 * t * t / (4 * u ** 3 * x ** 3) + 3 * t ** 3 / (4 * u ** 3 * x ** 4))
        chi, wm = expit(lam), expit(-lam)
        prod, odd = chi * wm, wm - chi
        beta = 4 * prod
        bjets = np.array([beta, beta * odd * lu,
            beta * ((1 - 6 * prod) * lu * lu + odd * luu),
            beta * (odd * (1 - 12 * prod) * lu ** 3 + 3 * (1 - 6 * prod) * lu * luu + odd * luuu)])

        def product_jets(coefficients):
            p = self.polynomial_jets(u, coefficients)
            return np.array([bjets[0] * p[0], bjets[1] * p[0] + bjets[0] * p[1],
                bjets[2] * p[0] + 2 * bjets[1] * p[1] + bjets[0] * p[2],
                bjets[3] * p[0] + 3 * bjets[2] * p[1] + 3 * bjets[1] * p[2] + bjets[0] * p[3]])

        alpha, alpha_u, alpha_uu, alpha_uuu = product_jets(self.q[64:72])
        _, Zu, Zuu, Zuuu = product_jets(self.q[72:80])
        r0, r0u, r0uu = RC + ELL / root, -.1 * u ** -1.5, .15 * u ** -2.5
        su, suu = -r0u, -r0uu
        alpha_s = 10 * u ** 1.5 * alpha_u
        alpha_su = 15 * root * alpha_u + 10 * u ** 1.5 * alpha_uu
        alpha_suu = 7.5 / root * alpha_u + 30 * root * alpha_uu + 10 * u ** 1.5 * alpha_uuu
        A = r0 * alpha_s
        Au = r0u * alpha_s + r0 * alpha_su
        Auu = r0uu * alpha_s + 2 * r0u * alpha_su + r0 * alpha_suu
        B = 10 * u ** 1.5 * Zu
        Bu = 15 * root * Zu + 10 * u ** 1.5 * Zuu
        Buu = 7.5 / root * Zu + 30 * root * Zuu + 10 * u ** 1.5 * Zuuu
        lw = math.log(AMP) - root * (2 - np.sin(u))
        lwu = root * np.cos(u) - (2 - np.sin(u)) / (2 * root)
        lwuu = np.cos(u) / root - root * np.sin(u) + (2 - np.sin(u)) / (4 * u ** 1.5)
        w0 = np.exp(lw)
        if not w0 > 0:
            raise TailChartBoundary("actual tail weight underflow: no zero-weight substitution allowed")
        b = B / w0
        bu = Bu / w0 - b * lwu
        buu = Buu / w0 - 2 * lwu * Bu / w0 + (lwu * lwu - lwuu) * b
        if 1 - A <= 0 or 1 + b <= 0:
            raise TailChartBoundary("actual a_s or z_s left the positive-radius-graph chart at u=" + repr(u))
        d = np.log1p(b) + 6 * alpha - 2 * np.log1p(-A)
        du = bu / (1 + b) + 6 * alpha_u + 2 * Au / (1 - A)
        duu = (buu / (1 + b) - bu * bu / (1 + b) ** 2 + 6 * alpha_uu
               + 2 * Auu / (1 - A) + 2 * Au * Au / (1 - A) ** 2)
        g0 = lwu + 1.5 / u + 8 * r0u / r0
        gp0 = lwuu - 1.5 / u ** 2 + 8 * (r0uu / r0 - (r0u / r0) ** 2)
        epsilon = .12 * (1 - A) ** 2 / (r0 * r0 * u ** 3)
        elog = -3 / u - 2 * r0u / r0 - 2 * Au / (1 - A)
        r = r0 * np.exp(alpha)
        logru = r0u / r0 + alpha_u
        ru = r * logru
        ruu = r * (logru * logru + r0uu / r0 - (r0u / r0) ** 2 + alpha_uu)
        weff = w0 * (1 + b) / (np.exp(alpha) * (1 - A))
        weff_u = weff * (lwu + bu / (1 + b) - alpha_u + Au / (1 - A))
        return {"r": r, "r_u": ru, "r_uu": ruu, "s_u": su, "s_uu": suu,
                "s": LENGTH - ELL / root, "epsilon": epsilon, "epsilon_log_u": elog,
                "g": g0 + du, "g_u": gp0 + duu,
                "log_P": 1.5 * np.log(u) + 8 * np.log(r0) - root * (2 - np.sin(u)) + d,
                "log_weight_perturbation_jets": [d, du, duu],
                "w_eff": weff, "w_eff_u": weff_u,
                "a_s": ru / su, "z_s": w0 * (1 + b)}

    def maximum_point(self, n):
        if n < FIRST_PEAK:
            raise ValueError("R582 proved stationary-point bracket begins at 160")
        if n not in self.maxima:
            center = np.pi / 2 + 2 * np.pi * n
            self.maxima[n] = brentq(lambda u: self.coefficients(u)["g"], center - .003, center,
                                    xtol=5e-13, rtol=4 * np.finfo(float).eps)
        return self.maxima[n]

    def integrate(self, left, right, state, args, *, inner=False, dense=False, factor=1):
        def rhs(u, value):
            COUNTS["inner_RHS" if inner else "outer_RHS"] += 1
            c = self.coefficients(u)
            y, z = value
            return [c["epsilon"] * z, -y - (c["g"] + c["epsilon_log_u"]) * z]
        sol = solve_ivp(rhs, (left, right), state, method="DOP853",
                        rtol=args.rtol / factor, atol=args.atol / factor,
                        max_step=args.max_step, dense_output=dense)
        if not sol.success or not np.all(np.isfinite(sol.y[:, -1])):
            raise ArithmeticError("actual-weight linear transfer failed: " + sol.message)
        return sol

    def inner_slope(self, M, args, factor=1):
        if M < FIRST_PEAK + 1:
            raise ValueError("finite tail input needs M>=161")
        state = np.array([0., 1.])
        high = self.maximum_point(M + 1)
        records, rho161 = [], None
        for n in range(M, FIRST_PEAK - 1, -1):
            low = self.maximum_point(n)
            incoming_y = float(state[0])
            sol = self.integrate(high, low, state, args, inner=True, factor=factor)
            outgoing = sol.y[:, -1]
            scale = float(outgoing[0])
            if scale == 0 or not np.isfinite(scale):
                raise ArithmeticError("actual-weight peak normalization lost y")
            rho = -incoming_y / scale
            if n < M and not 0 < rho < 1 / 32:
                raise ArithmeticError("actual-weight finite ratio contradicted the proved invariant interval")
            if n == FIRST_PEAK:
                rho161 = rho
            records.append({"cell": n, "rho": rho, "balanced_slope": float(outgoing[1] / scale),
                            "nfev": int(sol.nfev)})
            state, high = outgoing / scale, low
            self.last_completed = {"phase": "inner_backward_cell", "M": M, "cell": n,
                "u": high, "normalized_y_z": state.tolist(), "factor": factor,
                "normalization_y": 1., "not_a_complete_seed": True}
        return {"M": M, "terminal_peak": M + 1, "alpha160": self.maximum_point(FIRST_PEAK),
                "y_alpha160": 1., "z_alpha160": float(state[1]), "rho161": float(rho161),
                "exact_DtN_rho161_truncation_log_bound": -math.log(32) - 3 * (M - FIRST_PEAK) * math.log(10),
                "numerical_ODE_error_not_in_that_bound": True, "cell_records": records}

    def field_jets(self, u, state):
        c = self.coefficients(u)
        r, ru, ruu, su, suu = (c[k] for k in ("r", "r_u", "r_uu", "s_u", "s_uu"))
        y, z = state
        yu = c["epsilon"] * z
        yuu = -c["g"] * yu - c["epsilon"] * y
        C = r ** 4 * y
        Cu = 4 * r ** 3 * ru * y + r ** 4 * yu
        Cuu = ((12 * r * r * ru * ru + 4 * r ** 3 * ruu) * y
                + 8 * r ** 3 * ru * yu + r ** 4 * yuu)
        Cs, Css = Cu / su, Cuu / su ** 2 - Cu * suu / su ** 3
        # This form cancels 4f-r*f_r analytically, not by subtracting close floats.
        A = -c["w_eff"] * r ** 5 * yu / (3 * ru)
        As = c["w_eff"] * Cs
        Ass = c["w_eff_u"] / su * Cs + c["w_eff"] * Css
        return np.array([A, As, Ass, C, Cs, Css])

    def outward(self, inner, args, factor=1):
        alpha = inner["alpha160"]
        low_goal = (ELL / (LENGTH - TAIL_MOUTH)) ** 2
        centers = np.pi / 2 + 2 * np.pi * np.arange(FIRST_PEAK + 1)
        stops = np.r_[np.sort(centers[(centers < alpha) & (centers > low_goal)])[::-1], low_goal]
        high, state, log_scale = alpha, np.array([1., inner["z_alpha160"]]), 0.
        segments, chart_checkpoint = [], None
        for low in stops:
            try:
                sol = self.integrate(float(high), float(low), state, args, factor=factor)
            except TailChartBoundary as error:
                chart_checkpoint = str(error)
                break
            outgoing = sol.y[:, -1]
            scale = float(np.max(abs(outgoing)))
            if not scale > 0 or not np.isfinite(scale):
                raise ArithmeticError("actual outward projective transfer lost scale")
            state, high = outgoing / scale, float(low)
            log_scale += math.log(scale)
            segments.append({"u": high, "nfev": int(sol.nfev), "log_scale": log_scale})
            self.last_completed = {"phase": "outer_completed_cell", "u": high,
                "normalized_y_z": state.tolist(), "canonical_log_scale": log_scale,
                "inner": inner, "factor": factor, "not_a_complete_core_return": True}
        jets = self.field_jets(high, state)
        c = self.coefficients(high)
        width = c["s"] - CORE_END
        norm = float(np.max(abs(jets) * np.array([1, width, width ** 2, 1, width, width ** 2])))
        if not norm > 0:
            raise ArithmeticError("actual seed mouth C2 normalization vanished")
        return {"mouth_s": c["s"], "mouth_r": c["r"], "mouth_u": high,
                "mouth_a_s": c["a_s"], "mouth_z_s": c["z_s"],
                "normalized_jets_A_As_Ass_C_Cs_Css": (jets / norm).tolist(),
                "canonical_to_mouth_C2_log_scale": log_scale + math.log(norm),
                "chart_checkpoint_before_requested_mouth": chart_checkpoint,
                "requested_mouth_reached": chart_checkpoint is None,
                "actual_weight_jets_at_mouth": c["log_weight_perturbation_jets"],
                "segments": segments, "finite_transfer_is_not_interval_certified": True}


def compact_bump(s):
    """C-infinity support in (.06,.80); exact zero throughout the tail mouth."""
    s = np.asarray(s, dtype=float)
    t = (s - CONTROL_LEFT) / (CONTROL_RIGHT - CONTROL_LEFT)
    result = np.zeros((len(s), 3))
    active = (t > 0) & (t < 1)
    x = t[active]
    width = CONTROL_RIGHT - CONTROL_LEFT
    with np.errstate(under="ignore"):
        b = np.exp(4 - 1 / x - 1 / (1 - x))
    l1 = (x ** -2 - (1 - x) ** -2) / width
    l2 = (-2 * x ** -3 - 2 * (1 - x) ** -3) / width ** 2
    result[active] = np.column_stack((b, b * l1, b * (l1 * l1 + l2)))
    return result


class MeanProfile:
    """Frozen actual circular mean plus two newly declared compact controls."""
    def __init__(self, positions, q=SOURCE_Q):
        self.s = np.asarray(positions, dtype=float)
        if self.s[0] != 0 or self.s[-1] != LENGTH or not np.all(np.diff(self.s) > 0):
            raise ValueError("full background grid must strictly increase from 0 to L")
        self.par = physical.Parameters(p=.18, q=.18, offset=.2, ball_radius=1.012,
                                       strip_half_width=1 - .6 * 1.012, reach_target=.06 * 1.012)
        m = physical.Model(self.par, self.s, 32)
        COUNTS["background_grid_constructions"] += 1
        COUNTS["background_radial_points"] += len(self.s)
        self.tail_quadrature = m.tail_quadrature
        alpha, alpha_s, alpha_ss = (b @ q[64:72] for b in m.bases)
        Z, Zs, Zss = (b @ q[72:80] for b in m.bases)
        w, wm, wd, wdd = (a[:, 0] for a in (m.bg_w, m.bg_wm, m.bg_wd, m.bg_wdd))
        r0 = RC + LENGTH - self.s
        abase = wm * m.core["a0"] + w * r0
        abase_s = wd * (r0 - m.core["a0"]) - w
        abase_ss = wdd * (r0 - m.core["a0"]) - 2 * wd
        ea = np.exp(alpha)
        a = ea * abase
        ass = ea * (abase_ss + 2 * abase_s * alpha_s + abase * (alpha_ss + alpha_s * alpha_s))
        a_s = ea * (abase_s + abase * alpha_s)
        H, Hs, Hss = (v[:, 0] for v in (m.tail_height, m.tail_height1, m.tail_height2))
        central, tail = self.par.core_half_width + self.s, q[-1] + H
        z = wm * central + w * tail + Z
        zs = wm + wd * (tail - central) + w * Hs + Zs
        zss = -2 * wd + wdd * (tail - central) + 2 * wd * Hs + w * Hss + Zss
        self.base = (a, a_s, ass, z, zs, zss)
        self.bump = compact_bump(self.s)

    def jets(self, control, derivatives=True):
        nd = 2 if derivatives else 0
        D = physical.Dual
        def constant(v):
            v = np.asarray(v, dtype=float)
            return D(v, np.zeros(v.shape + (nd,)))
        mu, nu = constant(control[0]), constant(control[1])
        if nd:
            mu.d[0], nu.d[1] = 1., 1.
        a0, a1, a2, z0, z1, z2 = (constant(v) for v in self.base)
        psi, psis, psiss = self.bump.T
        alpha, alpha_s, alpha_ss = mu * psi, mu * psis, mu * psiss
        ea = alpha.exp()
        return (a0 * ea, ea * (a1 + a0 * alpha_s),
                ea * (a2 + 2 * a1 * alpha_s + a0 * (alpha_ss + alpha_s * alpha_s)),
                z0 + nu * psi, z1 + nu * psis, z2 + nu * psiss)

    def geometry_fields(self, control):
        a, ap, app, z, zp, zpp = self.jets(control)
        E = ap * ap + zp * zp
        speed = E.floor(1e-20) ** .5
        ks = (ap * zpp - zp * app) / speed ** 3
        kt = zp / (a * speed)
        R, Y, tau = self.par.ball_radius, self.par.strip_half_width, self.par.reach_target
        fields = {"ball": 1 - (a * a + z * z) / R ** 2,
                  "strip": 1 - a * a / Y ** 2,
                  "meridian_plus": 1 - tau * ks, "meridian_minus": 1 + tau * ks,
                  "orbit_plus": 1 - tau * kt, "orbit_minus": 1 + tau * kt,
                  "positive_height": (z - self.par.core_half_width) / tau,
                  "mean_E": E / .25 - 1, "det": E / .1 - 1,
                  "mirror": z * z / tau ** 2 - ap * ap / E.floor(1e-20)}
        return fields, (a, ap, app, z, zp, zpp, E, ks, kt)


class UndividedReturn:
    """C2 endpoint field ansatz and the two full equations, with no z_s division."""
    def __init__(self, profile, mouth, basis_count):
        self.profile, self.mouth, self.nb = profile, mouth, basis_count
        self.left, self.right = CORE_END, float(mouth["mouth_s"])
        if not self.right > CONTROL_RIGHT or basis_count < 6:
            raise ValueError("actual mouth must remain beyond the compact mean-control support")
        self.width = self.right - self.left
        self.indices = np.flatnonzero((profile.s >= self.left) & (profile.s <= self.right))
        self.s = profile.s[self.indices]
        x = (self.s - self.left) / self.width
        knots = np.r_[np.zeros(6), np.linspace(0, 1, basis_count - 4)[1:-1], np.ones(6)]
        B = BSpline(knots, np.eye(basis_count), 5, extrapolate=False)
        envelope = np.polynomial.Polynomial([0, 0, 0, 1, -3, 3, -1])
        ev = [envelope.deriv(k)(x) / self.width ** k for k in range(3)]
        b = [B(x, k) / self.width ** k for k in range(3)]
        free = [ev[0][:, None] * b[0],
                ev[1][:, None] * b[0] + ev[0][:, None] * b[1],
                ev[2][:, None] * b[0] + 2 * ev[1][:, None] * b[1] + ev[0][:, None] * b[2]]
        P = np.polynomial.Polynomial
        h00 = P([1, 0, 0, -10, 15, -6])
        h01, h11, h21 = P([0, 0, 0, 10, -15, 6]), P([0, 0, 0, -4, 7, -3]), P([0, 0, 0, .5, -1, .5])
        tail = np.asarray(mouth["normalized_jets_A_As_Ass_C_Cs_Css"])
        self.fixed, self.A_basis, self.C_basis = [], [], []
        for k in range(3):
            self.fixed.append(.5 * h00.deriv(k)(x) / self.width ** k)
            aj = sum(tail[j] * self.width ** j * h.deriv(k)(x) / self.width ** k
                     for j, h in enumerate((h01, h11, h21)))
            cj = sum(tail[3+j] * self.width ** j * h.deriv(k)(x) / self.width ** k
                     for j, h in enumerate((h01, h11, h21)))
            zero = np.zeros_like(free[k])
            self.A_basis.append(np.column_stack((aj, free[k], zero)))
            self.C_basis.append(np.column_stack((cj, zero, free[k])))

    def system(self, control):
        a, ap, _, _, zp, _ = self.profile.jets(control, derivatives=False)
        a, ap, zp = (v.v[self.indices] for v in (a, ap, zp))
        E = ap * ap + zp * zp
        if np.any(E <= 0):
            raise ArithmeticError("actual circular meridian lost immersion")
        # These are amplitudes of the full first variation of normalized E,F.
        first = 2 * (ap[:, None] * self.A_basis[1] + zp[:, None] * self.C_basis[1]) / E[:, None]
        second = -(a[:, None] * self.A_basis[1] + 3 * ap[:, None] * self.A_basis[0]
                   + 4 * zp[:, None] * self.C_basis[0]) / (2 * a * np.sqrt(E))[:, None]
        fixed1 = 2 * ap * self.fixed[1] / E
        fixed2 = -(a * self.fixed[1] + 3 * ap * self.fixed[0]) / (2 * a * np.sqrt(E))
        return np.vstack((first, second)), np.r_[fixed1, fixed2]

    def solve(self, control):
        COUNTS["linear_least_squares"] += 1
        matrix, fixed = self.system(control)
        scales = np.maximum(np.linalg.norm(matrix, axis=0), 1e-300)
        answer, _, rank, singular = np.linalg.lstsq(matrix / scales, -fixed, rcond=1e-13)
        coefficients = answer / scales
        residual = matrix @ coefficients + fixed
        normalized_normal = (matrix / scales).T @ residual
        normal = matrix.T @ residual
        return coefficients, {"rank": int(rank), "unknowns": int(len(coefficients)),
            "rcond": 1e-13,
            "retained_full_column_rank": bool(rank == len(coefficients)),
            "normalized_matrix_singular_max": float(singular[0]),
            "normalized_matrix_singular_min": float(singular[-1]),
            "normal_equation_residual_linf": float(np.max(abs(normal))),
            "normalized_normal_equation_residual_linf": float(np.max(abs(normalized_normal))),
            "reduced_control_gradient_is_certified": False,
            "reduced_control_gradient_scope": "explicit field-held derivative; variable-projection cancellation requires full least-squares stationarity and a differentiable constant-rank solution; rcond truncation or rank change need not satisfy it",
            "residual_l2_mean": float(np.mean(residual * residual)),
            "normalized_component_max": float(np.max(abs(residual))),
            "tail_amplitude": float(coefficients[0])}

    def evaluate(self, control, coefficients, derivatives=True):
        a, ap, _, _, zp, _ = self.profile.jets(control, derivatives=derivatives)
        # Indexing Dual explicitly preserves the control columns.
        D = physical.Dual
        def select(v):
            return D(v.v[self.indices], v.d[self.indices])
        a, ap, zp = (select(v) for v in (a, ap, zp))
        A = [f + b @ coefficients for f, b in zip(self.fixed, self.A_basis)]
        C = [b @ coefficients for b in self.C_basis]
        E = ap * ap + zp * zp
        e = 2 * (ap * A[1] + zp * C[1]) / E
        f = -(a * A[1] + 3 * ap * A[0] + 4 * zp * C[0]) / (2 * a * E ** .5)
        # e*cos(2 theta) and f*sin(2 theta) do not attain their absolute
        # amplitudes at the same angle. This entrywise amplitude expression
        # bounds the actual spectral norm; it is not its true angular peak.
        eta = .5 * (abs(e.v) + np.sqrt(e.v * e.v + 4 * f.v * f.v))
        score = .5 * float(np.mean(e.v * e.v + f.v * f.v))
        gradient = np.mean(e.v[:, None] * e.d + f.v[:, None] * f.d, axis=0)
        index = int(np.argmax(eta))
        report = {"first_variation_eta_max": float(eta[index]), "attainer_s": float(self.s[index]),
                  "conservative_angular_spectral_upper_bound": True,
                  "true_continuous_angular_maximum_computed": False,
                  "first_variation_normalized_E_max": float(np.max(abs(e.v))),
                  "first_variation_normalized_F_max": float(np.max(abs(f.v))),
                  "field_A_C_max": float(max(np.max(abs(A[0])), np.max(abs(C[0])))),
                  "field_s_first_max": float(max(np.max(abs(A[1])), np.max(abs(C[1])))),
                  "field_s_second_max": float(max(np.max(abs(A[2])), np.max(abs(C[2])))),
                  "undivided_two_equations_used_at_all_nodes": True,
                  "background_z_s_min": float(np.min(zp.v)),
                  "background_z_s_max": float(np.max(zp.v)),
                  "C2_endpoint_jets_matched_by_construction": True,
                  "nonlinear_isometry_not_asserted": True}
        return score, gradient, report


def full_geometry_report(profile, control):
    fields, values = profile.geometry_fields(control)
    a, _, _, z, _, _, E, ks, kt = values
    minima = {}
    for name, field in fields.items():
        i = int(np.argmin(field.v))
        minima[name] = {"value": float(field.v[i]), "s": float(profile.s[i])}
    violation = max(0., max(-p["value"] for p in minima.values()))
    return {"radial_nodes": len(profile.s), "geometry_violation_max": violation,
            "field_minima": minima, "radius_max": float(np.max(a.v)),
            "ball_max": float(np.max(np.sqrt(a.v * a.v + z.v * z.v))),
            "height_min": float(np.min(z.v)), "mean_E_min": float(np.min(E.v)),
            "curvature_max": float(max(np.max(abs(ks.v)), np.max(abs(kt.v)))),
            "finite_scan_only": True, "continuous_or_all_pair_reach_certified": False}


def source_input(raw):
    source = json.loads(raw)
    if source.get("schema") != "identified-circle-stage-zero-for-actual-flat-seed-v1":
        raise ValueError("actual circle input schema changed")
    for key in ("run_id", "job_id", "stage", "source_commit", "stage_JSON_sha256"):
        if source["origin"][key] != SOURCE[key]:
            raise ValueError("actual circle source identity changed: " + key)
    if not np.array_equal(np.asarray(source["q"], dtype=float), SOURCE_Q):
        raise ValueError("this declared actual seed must use the exact identified 17 mean coordinates")
    nodes = np.asarray(source["all_actual_and_pending_radial_nodes"], dtype=float)
    if len(nodes) < 5 or nodes[0] != 0 or nodes[-1] != LENGTH or not np.all(np.diff(nodes) > 0):
        raise ValueError("original actual/pending circle grid is invalid")
    return source, nodes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--M", type=int, default=168)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.15)
    parser.add_argument("--tolerance-refinement", type=float, default=8.)
    parser.add_argument("--return-basis", type=int, default=24)
    parser.add_argument("--return-radial-nodes", type=int, default=257)
    parser.add_argument("--geometry-radial-nodes", type=int, default=513)
    parser.add_argument("--maximum-control-iterations", type=int, default=60)
    parser.add_argument("--maximum-control-exchanges", type=int, default=4)
    parser.add_argument("--maximum-log-radius-control", type=float, default=.04)
    parser.add_argument("--maximum-height-control", type=float, default=.06)
    parser.add_argument("--maximum-seconds", type=float, default=1800.)
    args = parser.parse_args()
    if (not FIRST_PEAK < args.M <= 300 or args.tolerance_refinement <= 1
            or args.return_basis < 6 or args.return_radial_nodes < 33
            or args.geometry_radial_nodes < 65 or args.maximum_control_iterations < 1
            or args.maximum_control_exchanges < 1 or not 30 < args.maximum_seconds <= 2400
            or min(args.rtol, args.atol, args.max_step, args.maximum_log_radius_control,
                   args.maximum_height_control) <= 0):
        raise ValueError("invalid actual-circle seed and control scope")
    source, original_nodes = source_input(args.source_state_json)
    started = time.monotonic()
    deadline = started + args.maximum_seconds - 20
    actual = ActualTail(SOURCE_Q, deadline)
    definition = {"schema": SCHEMA, "source": source,
        "arguments": {k: v for k, v in vars(args).items() if k != "source_state_json"},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual_positive_weight": "P=z_s*a^8/(a_s^2*s_u), epsilon=12*(a_s*s_u)^2/a^2",
        "R582_proved_cell_start": 160,
        "compact_controls": {"support": [CONTROL_LEFT, CONTROL_RIGHT],
            "bump": "exp(4-1/t-1/(1-t)); exact zero outside 0<t<1",
            "radius": "a_actual*exp(mu*bump)", "height": "z_actual+nu*bump",
            "tail_seed_independent_of_controls": True},
        "linear_return": "a_s*A_s+z_s*C_s=0; a*A_s+3*a_s*A+4*z_s*C=0",
        "no_division_by_z_s_in_return_collocation": True,
        "conservative_angular_spectral_upper_bound": True,
        "true_continuous_angular_maximum_computed": False,
        "reduced_control_gradient_is_certified": False,
        "reduced_control_gradient_scope": "explicit field-held derivative, conditionally the variable-projection derivative at differentiable full least-squares stationarity; rcond truncation and rank changes are reported, not certified away",
        "C2_core_and_actual_tail_jets_enforced": True,
        "mean_profile_changes_the_design_metric": True,
        "fixed_metric_refinement_claim": False, "README_completion_claim": False}
    emit("ACTUAL_CIRCLE_DEFINITION", definition)
    latest_control, latest_linear, latest_scan = np.zeros(2), None, None
    seeds, comparisons, refinements = [], [], []
    seed, overall_best, overall_best_score = None, None, np.inf
    natural_results, accepted, outer_records = [], 0, []
    geometry_nodes = np.array([], dtype=float)
    actual_geometry_nodes = np.array([], dtype=float)
    actual_fine_geometry_nodes = np.array([], dtype=float)
    coarse_return_s = np.array([], dtype=float)
    fine_return_s = np.array([], dtype=float)
    pending = []

    def best_snapshot():
        return None if overall_best is None else {
            **overall_best, "control": overall_best["control"].tolist(),
            "coefficients": overall_best["coefficients"].tolist()}

    try:
        for M, factor in ((args.M, 1.), (args.M + 1, 1.), (args.M + 1, args.tolerance_refinement)):
            inner = actual.inner_slope(M, args, factor)
            outer = actual.outward(inner, args, factor)
            entry = {"M": M, "tolerance_factor": factor, "inner": inner, "outer": outer}
            seeds.append(entry)
            emit("ACTUAL_CIRCLE_SEED", entry)
        seed = seeds[-1]["outer"]
        for left, right in zip(seeds[:-1], seeds[1:]):
            same_mouth = left["outer"]["mouth_s"] == right["outer"]["mouth_s"]
            comparisons.append({"left_M": left["M"], "right_M": right["M"],
                "left_factor": left["tolerance_factor"], "right_factor": right["tolerance_factor"],
                "inner_balanced_slope_difference": right["inner"]["z_alpha160"] - left["inner"]["z_alpha160"],
                "same_actual_mouth": same_mouth,
                "C2_mouth_normalized_difference": (np.asarray(right["outer"]["normalized_jets_A_As_Ass_C_Cs_Css"])
                    - np.asarray(left["outer"]["normalized_jets_A_As_Ass_C_Cs_Css"])).tolist() if same_mouth else None,
                "comparison_is_not_a_numerical_error_certificate": True})
        emit("ACTUAL_CIRCLE_SEED_COMPARISONS", {"comparisons": comparisons,
            "all_actual_seed_and_comparison_cost_charged": True})
        mouth = float(seed["mouth_s"])
        if mouth <= CONTROL_RIGHT:
            raise ArithmeticError("actual seed mouth would overlap the fixed compact-control support")
        coarse_return_s = np.unique(np.r_[0., LENGTH, CORE_END, mouth,
                                          np.linspace(CORE_END, mouth, args.return_radial_nodes)])
        fine_return_s = np.unique(np.r_[coarse_return_s,
                                        (coarse_return_s[:-1] + coarse_return_s[1:]) / 2])
        return_profile = MeanProfile(coarse_return_s)
        fine_return_profile = MeanProfile(fine_return_s)
        return_operator = UndividedReturn(return_profile, seed, args.return_basis)
        fine_return_operator = UndividedReturn(fine_return_profile, seed, args.return_basis)
        phases = np.arange(4, 640) * (np.pi / 2)
        tail_points = LENGTH - ELL / np.sqrt(phases)
        geometry_nodes = np.unique(np.r_[original_nodes, np.linspace(0, LENGTH, args.geometry_radial_nodes),
                                         tail_points, CORE_END, .324, .612, .82, mouth])
        control = np.zeros(2)
        termination = "declared_compact_control_exchanges_returned"
        for outer_index in range(args.maximum_control_exchanges):
            actual.check_clock()
            geometry_profile = MeanProfile(geometry_nodes)
            fine_geometry_nodes = np.unique(np.r_[geometry_nodes,
                (geometry_nodes[:-1] + geometry_nodes[1:]) / 2])
            fine_geometry_profile = MeanProfile(fine_geometry_nodes)
            actual_geometry_nodes = geometry_nodes.copy()
            actual_fine_geometry_nodes = fine_geometry_nodes.copy()
            if overall_best is not None:
                carried = full_geometry_report(fine_geometry_profile, overall_best["control"])
                if carried["geometry_violation_max"] > 1e-8:
                    emit("ACTUAL_CIRCLE_REQUALIFICATION", {"outer": outer_index,
                        "previous_finite_candidate_lost_new_grid_qualification": True,
                        "control": overall_best["control"].tolist(), "new_fine_geometry": carried})
                    overall_best, overall_best_score = None, np.inf
                else:
                    overall_best["fine_geometry"] = carried
                    overall_best["qualified_fine_geometry_nodes"] = fine_geometry_nodes.tolist()
            cache = {}
            pending = []

            def candidate(value):
                actual.check_clock()
                key = np.asarray(value, dtype=float).tobytes()
                if key not in cache:
                    COUNTS["mean_control_candidates"] += 1
                    coefficients, linear = return_operator.solve(value)
                    score, gradient, report = return_operator.evaluate(value, coefficients)
                    fields, _ = geometry_profile.geometry_fields(value)
                    cache[key] = {"coefficients": coefficients, "linear": linear,
                        "score": score, "gradient": gradient, "report": report,
                        "geometry_values": np.concatenate([f.v for f in fields.values()]),
                        "geometry_jacobian": np.concatenate([f.d for f in fields.values()])}
                return cache[key]

            def assess(value, *, terminal=False):
                nonlocal overall_best, overall_best_score, accepted
                nonlocal latest_control, latest_linear, latest_scan
                item = candidate(value)
                _, _, fine_linear = fine_return_operator.evaluate(value, item["coefficients"])
                full = full_geometry_report(fine_geometry_profile, value)
                field_values, _ = fine_geometry_profile.geometry_fields(value)
                for name, field in field_values.items():
                    worst = int(np.argmin(field.v))
                    s = float(fine_geometry_profile.s[worst])
                    if field.v[worst] < -1e-8 and np.min(abs(geometry_nodes - s)) > 1e-12:
                        pending.append(s)
                feasible = full["geometry_violation_max"] <= 1e-8
                fine_score = fine_linear["first_variation_eta_max"]
                take = feasible and fine_score < overall_best_score
                if take:
                    overall_best = {"control": np.asarray(value, dtype=float).copy(),
                        "coefficients": item["coefficients"].copy(), "fine_linear": fine_linear,
                        "fine_geometry": full, "coarse_linear": item["linear"],
                        "qualified_fine_geometry_nodes": fine_geometry_nodes.tolist()}
                    overall_best_score = fine_score
                    accepted += 1
                latest_control, latest_linear, latest_scan = np.asarray(value, dtype=float).copy(), fine_linear, full
                emit("ACTUAL_CIRCLE_CONTROL_ITERATE", {
                    "outer": outer_index, "control": np.asarray(value).tolist(),
                    "terminal_OptimizeResult_point": terminal, "linear_fit": item["linear"],
                    "coarse_objective": item["score"], "fine_linear": fine_linear,
                    "fine_geometry": full, "accepted_finite_geometry_and_linear_improvement": take,
                    "pending_radial_geometry_positions": sorted(set(pending)),
                    "elapsed_seconds": time.monotonic() - started})

            assess(control)
            outcome = minimize(lambda v: candidate(v)["score"], control,
                jac=lambda v: candidate(v)["gradient"], method="SLSQP",
                bounds=[(-args.maximum_log_radius_control, args.maximum_log_radius_control),
                        (-args.maximum_height_control, args.maximum_height_control)],
                constraints={"type": "ineq", "fun": lambda v: candidate(v)["geometry_values"],
                             "jac": lambda v: candidate(v)["geometry_jacobian"]},
                callback=lambda v: assess(v),
                options={"maxiter": args.maximum_control_iterations, "ftol": 1e-13, "disp": False})
            natural = {"status": int(outcome.status), "success": bool(outcome.success),
                "message": str(outcome.message), "nit": int(outcome.nit),
                "nfev": int(outcome.nfev), "njev": int(outcome.njev),
                "control": outcome.x.tolist(), "not_an_exact_resonance_certificate": True}
            natural_results.append(natural)
            assess(outcome.x, terminal=True)
            outer_records.append({"outer": outer_index, "actual_geometry_nodes": geometry_nodes.tolist(),
                "actual_return_basis": args.return_basis, "natural_backend": natural,
                "pending_geometry_nodes": sorted(set(pending))})
            control = (overall_best["control"].copy() if overall_best is not None else outcome.x.copy())
            if not pending:
                termination = "natural_control_backend_returned_without_new_fine_geometry_points"
                break
            geometry_nodes = np.unique(np.r_[geometry_nodes, pending])
        if overall_best is not None:
            # Freeze this mean profile before enlarging only the linear field
            # representation. This is a linear-return observation, not a
            # finite nonlinear fixed-metric convergence claim.
            for count in (2 * args.return_basis, 4 * args.return_basis):
                actual.check_clock()
                refined = UndividedReturn(return_profile, seed, count)
                refined_fine = UndividedReturn(fine_return_profile, seed, count)
                coeff, linear = refined.solve(overall_best["control"])
                _, _, report = refined_fine.evaluate(overall_best["control"], coeff)
                refinements.append({"basis_count": count, "linear_fit": linear,
                    "report": report, "coefficients": coeff.tolist(),
                    "fit_radial_nodes": len(refined.s),
                    "independent_fine_radial_nodes": len(refined_fine.s),
                    "same_frozen_mean_controls": overall_best["control"].tolist(),
                    "finite_nonlinear_isometry_not_claimed": True})
        final = {"schema": SCHEMA, "termination": termination,
            "definition": definition, "actual_seed_mouth": seed,
            "mean_control_scope": [CONTROL_LEFT, CONTROL_RIGHT],
            "best_finite_geometry_qualified_linear_candidate": best_snapshot(),
            "last_trial_control": latest_control.tolist(), "last_trial_linear": latest_linear,
            "last_trial_geometry": latest_scan, "natural_OptimizeResults": natural_results,
            "accepted_finite_linear_improvements": accepted, "outer_records": outer_records,
            "last_constructed_geometry_nodes": actual_geometry_nodes.tolist(),
            "last_constructed_fine_geometry_nodes": actual_fine_geometry_nodes.tolist(),
            "pending_geometry_nodes": sorted(set(pending)),
            "next_geometry_node_proposal": np.unique(np.r_[geometry_nodes, pending]).tolist(),
            "proposal_is_not_an_already_optimized_grid": True,
            "fixed_mean_linear_representation_refinements": refinements,
            "counts": dict(COUNTS), "total_new_scientific_seconds": time.monotonic() - started,
            "actual_complete_linear_return_proved": False,
            "finite_isometric_family_constructed": False, "README_completion_claim": False}
        emit("ACTUAL_CIRCLE_FINAL", final)
        raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        emit("ACTUAL_CIRCLE_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    except ClockCheckpoint as error:
        emit("ACTUAL_CIRCLE_CLOCK_CHECKPOINT", {"schema": SCHEMA, "message": str(error),
            "definition": definition,
            "actual_seed_last_completed": actual.last_completed,
            "completed_seed_evaluations": seeds,
            "completed_seed_comparisons": comparisons,
            "actual_seed_mouth": seed,
            "best_finite_geometry_qualified_linear_candidate": best_snapshot(),
            "accepted_finite_linear_improvements": accepted,
            "last_constructed_geometry_nodes": actual_geometry_nodes.tolist(),
            "last_constructed_fine_geometry_nodes": actual_fine_geometry_nodes.tolist(),
            "fit_return_nodes": coarse_return_s.tolist(),
            "fine_return_nodes": fine_return_s.tolist(),
            "pending_geometry_nodes": sorted(set(pending)),
            "next_geometry_node_proposal": np.unique(np.r_[geometry_nodes, pending]).tolist(),
            "proposal_is_not_an_already_optimized_grid": True,
            "natural_OptimizeResults": natural_results, "outer_records": outer_records,
            "fixed_mean_linear_representation_refinements": refinements,
            "last_trial_control": latest_control.tolist(), "last_trial_linear": latest_linear,
            "last_trial_geometry": latest_scan, "counts": dict(COUNTS),
            "total_new_scientific_seconds": time.monotonic() - started,
            "README_completion_claim": False})


if __name__ == "__main__":
    main()
