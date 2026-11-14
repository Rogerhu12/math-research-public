#!/usr/bin/env python3
"""Local mixed-mode annulus via Gauss--Codazzi and Gauss--Weingarten.

This constructs a bounded strip, not the closed surface requested by the topic.
All inputs and the target metric remain fixed when --angles is increased.
Only small scalar diagnostics are printed; no mesh or large arrays are printed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


def initial_field(angles: int, amp2: float, amp3: float) -> tuple[np.ndarray, np.ndarray]:
    if abs(amp2) + abs(amp3) >= 1:
        raise ValueError("Positive radius requires |amp2|+|amp3|<1")
    theta = np.arange(angles) * (2 * np.pi / angles)
    phi = theta.copy()
    for _ in range(30):
        rho = 1 + amp2 * np.cos(2 * phi) + amp3 * np.cos(3 * phi)
        defect = phi + amp2 * np.sin(2 * phi) / 2 + amp3 * np.sin(3 * phi) / 3 - theta
        step = defect / rho
        phi -= step
        if np.max(np.abs(step)) < 3e-15:
            break
    rho = 1 + amp2 * np.cos(2 * phi) + amp3 * np.cos(3 * phi)
    x = ((1 + amp2 / 2) * np.sin(phi) + amp2 * np.sin(3 * phi) / 6
         + amp3 * np.sin(4 * phi) / 8 + amp3 * np.sin(2 * phi) / 4)
    y = ((-1 + amp2 / 2) * np.cos(phi) - amp2 * np.cos(3 * phi) / 6
         + amp3 * np.cos(2 * phi) / 4 - amp3 * np.cos(4 * phi) / 8
         - amp2 * amp3 / 24)
    state = np.zeros((14, angles))
    state[1] = 1 / rho  # M=0, N=a0^2/rho, a0=1.
    state[2] = x
    state[3] = y
    state[7] = 1  # e1=(0,0,1)
    state[8] = np.cos(phi)
    state[9] = np.sin(phi)  # e2=T
    state[11] = -np.sin(phi)
    state[12] = np.cos(phi)  # n=e1 cross e2
    return theta, state


def diff_theta(values: np.ndarray) -> np.ndarray:
    n = values.shape[-1]
    k = np.fft.fftfreq(n, d=1 / n)
    # The real even-grid Nyquist mode has zero sampled first derivative.
    if n % 2 == 0:
        k[n // 2] = 0
    return np.fft.ifft(1j * k * np.fft.fft(values, axis=-1), axis=-1).real


def background(s: float, curvature: float) -> tuple[float, float, float]:
    return 1 + curvature * s * s / 2, curvature * s, curvature


def rhs(s: float, flat: np.ndarray, angles: int, curvature: float) -> np.ndarray:
    q = flat.reshape(14, angles)
    m, nn = q[:2]
    a, ap, app = background(s, curvature)
    if np.min(nn) <= 1e-10:
        raise FloatingPointError("GC normal form reached N=0; this branch cannot continue by division")
    ell = (m * m - a * app) / nn
    e1, e2, normal = q[5:8], q[8:11], q[11:14]
    out = np.zeros_like(q)
    out[0] = diff_theta(ell) - ap * m / a
    out[1] = diff_theta(m) + ap * nn / a + a * ap * ell
    out[2:5] = e1
    out[5:8] = ell * normal
    out[8:11] = (m / a) * normal
    out[11:14] = -ell * e1 - (m / a) * e2
    return out.ravel()


def diagnostics(s: float, q: np.ndarray, curvature: float) -> dict:
    m, nn = q[:2]
    a, ap, app = background(s, curvature)
    ell = (m * m - a * app) / nn
    x, e1, e2, normal = q[2:5], q[5:8], q[8:11], q[11:14]
    xt = diff_theta(x)
    metric = np.empty((q.shape[1], 2, 2))
    metric[:, 0, 0] = np.sum(e1 * e1, axis=0) - 1
    metric[:, 0, 1] = metric[:, 1, 0] = np.sum(e1 * xt, axis=0) / a
    metric[:, 1, 1] = np.sum(xt * xt, axis=0) / (a * a) - 1
    shape = np.empty_like(metric)
    shape[:, 0, 0] = ell
    shape[:, 0, 1] = shape[:, 1, 0] = m / a
    shape[:, 1, 1] = nn / (a * a)
    frame = np.stack((e1, e2, normal), axis=1).transpose(2, 0, 1)
    frame_defect = np.einsum('nij,nkj->nik', frame, frame) - np.eye(3)
    # For a true parallel circular collar one needs N=a*z', M=0,
    # e1 radial/vertical, all noncircular position modes zero, and full jets.
    center = x.mean(axis=1)
    radius = np.linalg.norm(x[:2] - center[:2, None], axis=0)
    return {
        "s": float(s), "radius_metric": float(a),
        "center": center.tolist(),
        "sample_relative_metric_op": float(np.max(np.abs(np.linalg.eigvalsh(metric)))),
        "sample_position_frame_compatibility": float(np.max(np.linalg.norm(xt - a * e2, axis=0))),
        "sample_frame_orthogonality": float(np.max(np.abs(frame_defect))),
        "sample_abs_principal_curvature": float(np.max(np.abs(np.linalg.eigvalsh(shape)))),
        "sample_min_N": float(np.min(nn)),
        "sample_circle_radial_spread": float(np.ptp(radius)),
        "sample_section_height_spread": float(np.ptp(x[2])),
        "sample_max_abs_M": float(np.max(np.abs(m))),
        "sample_GC_N_spread": float(np.ptp(nn)),
    }


def run(args: argparse.Namespace) -> dict:
    theta, initial = initial_field(args.angles, args.amp2, args.amp3)
    ts = np.linspace(0, args.end, args.samples)
    started = time.perf_counter()
    solution = solve_ivp(
        lambda s, y: rhs(s, y, args.angles, args.curvature),
        (0, args.end), initial.ravel(), method="DOP853", t_eval=ts,
        rtol=args.rtol, atol=args.atol, max_step=args.max_step,
    )
    records = [diagnostics(float(s), flat.reshape(14, args.angles), args.curvature)
               for s, flat in zip(solution.t, solution.y.T)]
    if not records:
        raise RuntimeError(solution.message)
    expected = np.array([0., -args.curvature * args.amp2 * args.amp3 / 2, 0.])
    # Exact initial second derivative from the normal form, independent of time stepping.
    nn = initial[1]
    ell0 = -args.curvature / nn
    numerical_c2 = np.mean(ell0 * initial[11:14], axis=1)
    payload = {
        "status": "local_annulus_numerical_evidence_only",
        "closed_surface": False, "double_circular_collars": False,
        "whole_family_reach_certified": False, "task_complete": False,
        "definition": {"rho": "1+A*cos(2*phi)+B*cos(3*phi)",
                       "metric": "ds^2+(1+k*s^2/2)^2*dtheta^2",
                       "target_frozen_with_respect_to_angles": True,
                       "A": args.amp2, "B": args.amp3, "k": args.curvature,
                       "s_interval": [0, args.end]},
        "discretization": {"angles": args.angles, "samples": args.samples,
                           "rtol": args.rtol, "atol": args.atol,
                           "max_step": args.max_step},
        "solver": {"success": bool(solution.success), "message": solution.message,
                   "nfev": solution.nfev, "elapsed_seconds": time.perf_counter() - started},
        "initial_center_second_derivative_exact": expected.tolist(),
        "initial_center_second_derivative_sample": numerical_c2.tolist(),
        "sample_initial_c2_error": float(np.max(np.abs(expected - numerical_c2))),
        "sample_max_metric": max(r["sample_relative_metric_op"] for r in records),
        "sample_max_curvature": max(r["sample_abs_principal_curvature"] for r in records),
        "records": records,
        "limitations": [
            "Open local annulus; no cap or exact circular exit has been obtained.",
            "All reported spatial metrics are Fourier-grid samples, not continuous certificates.",
            "The center drift is a material-angle mean, not a Hausdorff displacement bound.",
            "The principal-curvature diagnostic does not give global reach.",
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.state_out:
        target = Path(args.state_out)
        target.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(target, theta=theta, s=solution.t, state=solution.y)
        payload["state_file"] = str(target)
        payload["state_sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--angles", type=int, default=96)
    parser.add_argument("--amp2", type=float, default=.25)
    parser.add_argument("--amp3", type=float, default=.2)
    parser.add_argument("--curvature", type=float, default=.6)
    parser.add_argument("--end", type=float, default=.35)
    parser.add_argument("--samples", type=int, default=15)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.005)
    parser.add_argument("--out", required=True)
    parser.add_argument("--state-out")
    args = parser.parse_args()
    if args.angles < 16 or args.end <= 0 or args.curvature <= 0:
        parser.error("Require angles>=16, end>0, curvature>0 for this local hyperbolic experiment")
    payload = run(args)
    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")
    last = payload["records"][-1]
    print(json.dumps({"out": str(target), "success": payload["solver"]["success"],
                      "angles": args.angles, "metric_sample": payload["sample_max_metric"],
                      "initial_c2_error": payload["sample_initial_c2_error"],
                      "exit_center": last["center"], "exit_radius_spread": last["sample_circle_radial_spread"],
                      "seconds": payload["solver"]["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
