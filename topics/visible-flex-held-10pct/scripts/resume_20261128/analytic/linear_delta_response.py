#!/usr/bin/env python3
"""Measure R72's complete linear port derivative on the actual restored profile.

This is a two-dimensional rotation-background calculation, not a finite-amplitude
BVP, a true nonlinear tail, or an interval proof.  The complete fixed bridge and
the literal restored DN port are included.  All large trajectories stay in
scratch; only scalar diagnostics and input hashes are written.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def matrix(v, m):
    b = math.sqrt(1-v*v)
    q = m*m
    return np.array([[-(q-1)*v, -q*b], [(q-1)*v*v/b, q*v]])


def integrate_pieces(rhs, knots, state, rtol):
    last = np.asarray(state, float)
    calls = 0
    for lo, hi in zip(knots[:-1], knots[1:]):
        if hi <= lo:
            raise ValueError("Non-positive integration interval")
        sol = solve_ivp(rhs, (lo, hi), last, method="DOP853",
                        rtol=rtol, atol=rtol*0.01,
                        max_step=(hi-lo)/12)
        if not sol.success:
            raise RuntimeError(sol.message)
        last = sol.y[:, -1]
        calls += sol.nfev
    return last, calls


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--mode-indices", default="1,2,3,4,6,8")
    p.add_argument("--rtol", type=float, default=2e-11)
    p.add_argument("--root-halfwidth", type=float, default=0.0001)
    args = p.parse_args()
    started = time.monotonic()
    topic = args.repo.resolve()/"topics/visible-flex-held-10pct"
    source = args.work.resolve()/"multistage-source"
    short = args.work.resolve()/"runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py"
    profile_file = topic/"scripts/resume_m3/multistage_profile_linear_root.json"
    chart_file = args.work.resolve()/"inputs/reference/chart.json"
    port_file = args.work.resolve()/"m24-linear-port.json"
    profile = json.loads(profile_file.read_text())
    chart = json.loads(chart_file.read_text())
    port = json.loads(port_file.read_text())
    port["cut"]["_prefix_bridge"] = profile["prefix_bridge"]
    record = {
        "command": ["linear_delta_response.py", "--source-topic", str(source),
                    "--short-bridge", str(short), "--profile", str(profile_file),
                    "--chart", str(chart_file), "--port", str(port_file)],
        "physical_profile": profile, "angular_chart": chart,
        "physical_tail_parameters": port["parameters"],
        "physical_tail_cut": port["cut"], "modes": 24, "angular": 64,
        "gauge_q": .06, "warp_reference": .06,
        "gates": {"physical_bc_tol": 2e-9, "bc_tol": 1e-7},
    }
    loader = module("held10_actual_linear_model", topic/"scripts/resume_m3/actual_m3_metric_model.py")
    obj = loader.load_model(record)
    base_delta = profile["delta"]
    delta_ref = float(__import__("fractions").Fraction(profile["multistage_flat"]["reference_delta"]))
    base_flow = obj.flow(0.)
    prefix_knots_ref = base_flow.breakpoints/(base_delta/delta_ref)
    bridge = base_flow.bridge
    bridge_knots = bridge.breakpoints
    jmat = np.array([[0., -1.], [1., 0.]])

    def calc(delta, mode_index, rtol=args.rtol):
        flow = obj.flow(float(delta-base_delta))
        m = int(flow.even[mode_index])
        ratio = delta/delta_ref
        endpoint_line = flow.linear_terminal(mode_index)
        c = float(endpoint_line[0])
        ell = np.array([1., -c])

        def prefix_rhs(xi, yy):
            aa, vv, _ = flow.prefix_profile(np.array([ratio*xi]))
            aa, vv = float(aa[0]), float(vv[0])
            mm = matrix(vv, m)
            a = ratio*mm/aa
            da = mm/(delta_ref*aa*aa)
            x, dx = yy[:2], yy[2:4]
            integral = float(x @ jmat @ mm @ x)/(aa**3)
            return np.r_[a @ x, a @ dx+da @ x, integral]

        prefix, prefix_calls = integrate_pieces(prefix_rhs, prefix_knots_ref,
                                                [1., 0., 0., 0., 0.], rtol)

        def bridge_rhs(s, yy):
            aa, vv, _ = bridge.profile(np.array([s]))
            aa, vv = float(aa[0]), float(vv[0])
            a = matrix(vv, m)/aa
            return np.r_[a @ yy[:2], a @ yy[2:4], vv/aa]

        finish, bridge_calls = integrate_pieces(bridge_rhs, bridge_knots,
                                                np.r_[prefix[:4], 0.], rtol)
        x, dx = finish[:2], finish[2:4]
        residual, derivative = float(ell @ x), float(ell @ dx)
        det_b = math.exp(finish[4])
        gamma = float(x[1])
        normalized = float(residual/np.linalg.norm(x)/np.linalg.norm(ell))
        # The R72 identity is a resonance identity. Do not attach it to the
        # nonresonant high modes merely because the quotient can be evaluated.
        resonant_comparison = mode_index == 0 and abs(normalized) < 1e-8 and gamma != 0
        resonant_formula = (det_b*prefix[4]/(delta_ref*gamma)
                            if resonant_comparison else None)
        return dict(delta=float(delta), mode=m, prefix_calls=prefix_calls,
                    bridge_calls=bridge_calls, robin_C=c,
                    response=residual, delta_derivative=derivative,
                    response_normalized=normalized,
                    cut_gamma=gamma, cut_norm=float(np.linalg.norm(x)),
                    bridge_determinant=det_b,
                    R72_prefix_integral=float(prefix[4]),
                    R72_comparison_is_near_resonance=bool(resonant_comparison),
                    R72_resonance_formula=resonant_formula,
                    formula_relative_discrepancy=(float(abs(derivative-resonant_formula)/max(1., abs(derivative)))
                        if resonant_formula is not None else None))

    bracket = [base_delta-args.root_halfwidth, base_delta+args.root_halfwidth]
    root = brentq(lambda delta: calc(delta, 0)["response_normalized"], *bracket,
                  xtol=3e-15, rtol=1e-14)
    roots = [calc(root, 0, args.rtol), calc(root, 0, args.rtol/10)]
    fd = []
    for step in (1e-5, 2e-6, 4e-7, 8e-8):
        plus, minus = calc(root+step, 0), calc(root-step, 0)
        d = (plus["response"]-minus["response"])/(2*step)
        fd.append(dict(step=step, finite_difference=d,
                       relative_error=float(abs(d-roots[0]["delta_derivative"])/abs(roots[0]["delta_derivative"]))))
    indices = [int(s)-1 for s in args.mode_indices.split(",")]
    rows = [calc(root, i) for i in indices]
    result = dict(status="linear_rotation_background_measured", scope=__doc__,
        root_delta=root, recorded_root_delta=base_delta,
        root_difference=float(root-base_delta), root_diagnostics=roots,
        finite_difference=fd, modes=rows, elapsed_seconds=time.monotonic()-started,
        source_hashes={str(file):sha(file) for file in
            (profile_file, chart_file, port_file, short,
             source/"notes/fixed_metric_mode3_flow.py",
             source/"scripts/held10_multistage_flat_profile.py")},
        new_finite_amplitude_bvp=False, interval_certificate=False,
        nonlinear_tail_solved=False, complete_surface=False)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(status=result["status"], root_delta=root,
        delta_derivative=roots[0]["delta_derivative"],
        R72_prefix_integral=roots[0]["R72_prefix_integral"],
        formula_relative_discrepancy=roots[0]["formula_relative_discrepancy"],
        elapsed_seconds=result["elapsed_seconds"])), flush=True)


if __name__ == "__main__":
    main()
