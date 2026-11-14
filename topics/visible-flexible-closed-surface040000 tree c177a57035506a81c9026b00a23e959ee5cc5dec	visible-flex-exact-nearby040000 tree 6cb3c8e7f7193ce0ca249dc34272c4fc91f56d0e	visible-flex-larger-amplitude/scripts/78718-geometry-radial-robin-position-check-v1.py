#!/usr/bin/env python3
"""Floating source/profile and physical-position cross-check of the radial scan.

No nonlinear solve, tail request, or current candidate data is used.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=Path, required=True)
    parser.add_argument("--scan", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve()
    main_path = here.with_name("78718-geometry-radial-robin-scan-v1.py")
    old_path = here.with_name("950f-prefix-flat-accel-screen.py")
    if sha(main_path) != "b3baa2244e6547f9f72b98e61d51f4fc3a51bbc2f191f65324e9b145f47eb863":
        raise ValueError("Frozen scan script changed")
    m = load(main_path, "frozen_radial_scan")
    old = load(old_path, "frozen_flat_accel_source")
    import numpy as np
    from scipy.integrate import solve_ivp
    if sha(args.port) != m.PORT_SHA:
        raise ValueError("Wrong frozen port")
    if args.report.exists():
        raise FileExistsError("Existing diagnostic output")
    port = json.loads(args.port.read_text())
    previous = json.loads(args.scan.read_text())
    bg = m.Background(64)
    us = np.unique(np.r_[np.linspace(0, 1, 1001), np.asarray(bg.cycle_knots[:8])/bg.tu])
    exact_source = np.stack(old.ramp(us, m.EPS, m.ETA), axis=-1)
    new_values = np.array([bg.ramp(float(u)) for u in us])
    profile_gap = float(np.max(np.abs(exact_source-new_values)))

    def propagate(profile, knots, n, state):
        state = np.asarray(state, dtype=float)
        state /= np.linalg.norm(state)

        def rhs(s, y):
            a, c, _ = profile(s)
            v = math.sqrt(1-c*c)
            return [(-(n*n-1)*c*y[0]-n*n*v*y[1])/a,
                    ((n*n-1)*c*c*y[0]/v+n*n*c*y[1])/a]

        for lo, hi in zip(knots, knots[1:]):
            sol = solve_ivp(rhs, (lo, hi), state, method="DOP853", rtol=3e-13, atol=3e-15,
                            max_step=abs(hi-lo)/80)
            if not sol.success:
                raise RuntimeError(sol.message)
            state = sol.y[:, -1]
            state /= np.linalg.norm(state)
        line = np.array([n*state[1], -state[0]])
        return line/np.linalg.norm(line)

    rows = []
    old_rows = {row["mode"]: row for row in previous["runs"][1]["rows"]}
    for n in (3, 39, 42, 45):
        index = n//3-1
        if port["modes"][index] != n:
            raise ValueError("Mode-index mismatch")
        dn = port["linearSlope"][index]
        left = propagate(bg.cycle, bg.cycle_knots, n, [1., 0.])
        right = propagate(bg.bridge, [bg.length, bg.length*bg.critical, 0.], n,
                          [-m.W*(m.CUT*dn-n*n)/(n*n-1), 1.])
        wr = abs(float(left[0]*right[1]-left[1]*right[0]))
        gap = abs(wr-old_rows[n]["abs_normalized_line_wronskian"])
        rows.append({"mode": n, "physical_position_abs_line_wronskian": wr,
                     "difference_from_projective_scan": gap})
    report = {
        "scope": "Floating numerical cross-check only; no rigorous spectral gap or current nonradial inverse.",
        "profile_samples": int(len(us)), "profile_max_abs_difference": profile_gap,
        "position_equation": "f_s=-[(n^2-1)c f+n^2v h]/a; h_s=[(n^2-1)c^2f/v+n^2c h]/a",
        "common_interface_map": "(X,Y) is proportional to (n*h,-f)",
        "rows": rows,
        "maximum_projective_position_difference": max(row["difference_from_projective_scan"] for row in rows),
        "sources": [{"path": str(p), "bytes": p.stat().st_size, "sha256": sha(p)}
                    for p in (here, main_path, old_path, args.port, args.scan)],
        "tail_requests": 0, "nonlinear_pde_runs": 0, "candidate_arrays_read": 0,
    }
    args.report.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"success": True, "profile_samples": report["profile_samples"],
                      "profile_max_abs_difference": profile_gap,
                      "maximum_projective_position_difference": report["maximum_projective_position_difference"],
                      "report_bytes": args.report.stat().st_size, "report_sha256": sha(args.report),
                      "script_sha256": sha(here)}, sort_keys=True))


if __name__ == "__main__":
    main()
