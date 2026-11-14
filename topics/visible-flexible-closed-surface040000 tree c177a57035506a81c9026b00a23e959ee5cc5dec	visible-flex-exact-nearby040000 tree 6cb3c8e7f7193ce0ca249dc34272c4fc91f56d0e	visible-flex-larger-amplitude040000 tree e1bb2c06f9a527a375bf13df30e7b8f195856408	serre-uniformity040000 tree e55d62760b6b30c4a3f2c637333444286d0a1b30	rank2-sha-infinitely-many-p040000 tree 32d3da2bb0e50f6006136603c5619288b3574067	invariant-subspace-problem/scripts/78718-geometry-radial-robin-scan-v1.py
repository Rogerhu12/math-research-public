#!/usr/bin/env python3
"""Exploratory fixed-background radial Robin scan using projective ODEs.

Reads only the frozen old linear-port file, not any candidate curve/CP/tail
array.  Does not issue a tail request or change any solver/candidate.  All
numerical outputs are floating diagnostics, not interval certificates or the
linearization of the current nonradial solution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time

for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


PORT_SHA = "500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702"
DELTA = float("0.07254443456654512")
VU, VD, EPS, ETA = float("0.17"), float("0.18"), float("0.4"), float("0.05")
CUT, W = float("0.6"), float("0.5")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Background:
    def __init__(self, quadrature: int):
        self.tu = DELTA / (VU * (1 - EPS))
        self.td = DELTA / (VD * (1 - EPS))
        self.cycle_end = self.tu + self.td
        x, w = np.polynomial.legendre.leggauss(quadrature)
        self.nodes = (x + 1) / 2
        self.weights = w / 2
        self.pt = math.pi / 2 - math.atan(W)
        self.ps = (-7 * W / CUT) / (1 + W * W) ** 1.5
        self.length = brentq(self.root_gap, .6, .7, xtol=5e-15, rtol=9e-16)
        self.d = -self.length * self.ps
        self.critical = 2 * (3 * self.pt + self.d) / (3 * (2 * self.pt + self.d))
        self.end = self.cycle_end + self.length
        unit = [0, EPS * ETA, EPS * (1-ETA), EPS, 1-EPS,
                1-EPS * (1-ETA), 1-EPS * ETA, 1]
        self.cycle_knots = sorted(set([self.tu * t for t in unit] +
                                     [self.tu + self.td * t for t in unit]))

    def phase(self, t, length):
        d = -length * self.ps
        return (3 * self.pt + d) * t * t - (2 * self.pt + d) * t * t * t

    def primitive(self, t, length):
        return t * float(self.weights @ np.sin(self.phase(t * self.nodes, length)))

    def root_gap(self, length):
        return length * self.primitive(1.0, length) - (1 - CUT)

    @staticmethod
    def ramp(u):
        if u < EPS:
            t, side = u / EPS, 1
        elif u > 1 - EPS:
            t, side = (1 - u) / EPS, -1
        else:
            return 1.0, u - EPS / 2, 0.0
        t = min(1.0, max(0.0, t))
        z = min(t, 1 - t)
        x = z / ETA
        if z < ETA:
            fsmall = ETA / (1-ETA) * (x**3 - x**4/2)
            psmall = ETA**2 / (1-ETA) * (x**4/4 - x**5/10)
            accel = (3*x*x - 2*x**3) / (1-ETA)
        else:
            fsmall = (z - ETA/2) / (1-ETA)
            psmall = (z*z/2 - ETA*z/2 + .15*ETA*ETA) / (1-ETA)
            accel = 1 / (1-ETA)
        f = fsmall if t <= .5 else 1 - fsmall
        prim = psmall if t <= .5 else .5 - (1-t) + psmall
        integ = EPS*prim if side == 1 else 1-EPS-EPS*prim
        return f, integ, side * accel / EPS

    def cycle(self, s):
        if s < self.tu:
            u, duration, speed, sign, offset = s/self.tu, self.tu, VU, 1, 1.0
        else:
            u, duration, speed, sign, offset = (s-self.tu)/self.td, self.td, VD, -1, 1+DELTA
        vel, integ, accel = self.ramp(u)
        return (offset + sign*DELTA*integ/(1-EPS),
                sign*speed*vel, sign*speed*accel/duration)

    def bridge(self, local_s):
        t = min(1.0, max(0.0, local_s/self.length))
        ph = self.phase(t, self.length)
        phs = (2*(3*self.pt+self.d)*t - 3*(2*self.pt+self.d)*t*t)/self.length
        return 1-self.length*self.primitive(t, self.length), -math.sin(ph), -math.cos(ph)*phs


def propagate(profile, knots, n, theta0, rtol, atol, divisions):
    state = np.array([theta0, 0.0])
    calls = 0

    def rhs(s, data):
        a, c, app = profile(s)
        v = math.sqrt(1-c*c)
        h = v/(a*a)
        hv = a*app/(v*v*v)
        sn, cs = math.sin(data[0]), math.cos(data[0])
        return [-n*(hv*cs*cs+h*sn*sn), n*(h-hv)*sn*cs]

    for lo, hi in zip(knots, knots[1:]):
        if lo == hi:
            continue
        sol = solve_ivp(rhs, (lo, hi), state, method="DOP853", rtol=rtol, atol=atol,
                        max_step=abs(hi-lo)/divisions)
        if not sol.success:
            raise RuntimeError(sol.message)
        state = sol.y[:, -1]
        calls += sol.nfev
    return float(state[0]), float(state[1]), calls


def one_pass(port, count, settings):
    bg = Background(settings["quadrature"])
    rows = []
    for index in range(count):
        n = 3*(index+1)
        if port["modes"][index] != n:
            raise ValueError("Frozen mode-index identity mismatch")
        dn = float(port["linearSlope"][index])
        xcut, ycut = n*(CUT*dn-1), W*(CUT*dn-n*n)/CUT
        theta_cut = math.atan2(xcut, ycut)
        left, left_log, lcalls = propagate(bg.cycle, bg.cycle_knots, n, 0.0,
                                           settings["rtol"], settings["atol"], settings["divisions"])
        right, right_log, rcalls = propagate(bg.bridge, [bg.length, bg.length*bg.critical, 0.0],
                                             n, theta_cut, settings["rtol"], settings["atol"], settings["divisions"])
        delta = math.remainder(left-right, math.pi)
        rows.append({"mode": n, "phase_difference_mod_pi": delta,
                     "normalized_line_wronskian": math.sin(delta),
                     "abs_normalized_line_wronskian": abs(math.sin(delta)),
                     "left_log_euclidean_amplification": left_log,
                     "right_log_euclidean_amplification": right_log,
                     "ode_rhs_calls": lcalls+rcalls})
    return {"settings": settings, "bridge_length_float": bg.length,
            "bridge_root_gap_float": bg.root_gap(bg.length),
            "cycle_length_float": bg.cycle_end, "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--modes", type=int, default=21)
    args = parser.parse_args()
    if digest(args.port) != PORT_SHA:
        raise ValueError("Wrong frozen port")
    if args.report.exists():
        raise FileExistsError("Exploratory output prefix already used")
    port = json.loads(args.port.read_text())
    if not (port["parameters"]["rCut"] == CUT and port["parameters"]["wCut"] == W):
        raise ValueError("Frozen requested physical cut differs")
    if not (0 < args.modes <= len(port["linearSlope"])):
        raise ValueError("Mode range unavailable")
    start = time.monotonic()
    settings = [
        {"quadrature": 32, "rtol": 2e-10, "atol": 2e-12, "divisions": 30},
        {"quadrature": 64, "rtol": 2e-12, "atol": 2e-14, "divisions": 60},
    ]
    runs = [one_pass(port, args.modes, setting) for setting in settings]
    differences = [abs(a["normalized_line_wronskian"]-b["normalized_line_wronskian"])
                   for a, b in zip(runs[0]["rows"], runs[1]["rows"])]
    refined = runs[1]["rows"]
    least = min(refined, key=lambda row: row["abs_normalized_line_wronskian"])
    report = {
        "scope": "Floating exploratory radial-background Robin line comparison only; no rigorous gap or current nonradial inverse.",
        "equation": "theta_s=-n[(a*a_ss/v^3)cos(theta)^2+(v/a^2)sin(theta)^2], v=sqrt(1-a_s^2)",
        "left_boundary": "x(0)=0; X=x/i, y=Y, theta=atan2(X,Y)",
        "right_boundary": "X=n*(a*D_n-1), Y=w*(a*D_n-n^2)/a, sigma=-1",
        "match_location": "cycle/bridge common boundary a=1, a_s=0",
        "frozen_port_path": str(args.port.resolve()), "frozen_port_sha256": PORT_SHA,
        "frozen_port_raw_cut_slope_abs_diff": abs(port["cut"]["backgroundSlope"]-W),
        "parameters": {"delta_hex": DELTA.hex(), "vu_hex": VU.hex(), "vd_hex": VD.hex(),
                       "eps_hex": EPS.hex(), "eta_hex": ETA.hex(), "cut_hex": CUT.hex(), "w_hex": W.hex()},
        "script_sha256": digest(Path(__file__).resolve()),
        "runs": runs,
        "maximum_cross_refinement_wronskian_difference": max(differences),
        "smallest_refined_mode": least["mode"],
        "smallest_refined_abs_normalized_line_wronskian": least["abs_normalized_line_wronskian"],
        "seconds": time.monotonic()-start,
        "candidate_arrays_read": 0, "tail_requests": 0, "nonlinear_pde_runs": 0,
    }
    args.report.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    if args.report.stat().st_size >= 5_000_000:
        raise RuntimeError("Per-file size limit")
    brief = {"success": True, "scope": "floating_radial_background_only",
             "modes_scanned": args.modes, "smallest_mode": least["mode"],
             "smallest_abs_line_wronskian": least["abs_normalized_line_wronskian"],
             "cross_refinement_max_diff": max(differences),
             "selected_abs_line_wronskians": {str(row["mode"]):row["abs_normalized_line_wronskian"]
                    for row in refined if row["mode"] in (3, 39, 42, 45)},
             "report_bytes": args.report.stat().st_size, "report_sha256": digest(args.report),
             "script_sha256": report["script_sha256"], "seconds": report["seconds"]}
    print(json.dumps(brief, sort_keys=True))


if __name__ == "__main__":
    main()
