#!/usr/bin/env python3
"""Re-evaluate saved core-tail candidates; no optimization is performed.

This local development audit only diagnoses where an already published finite
candidate misses its designed metric. It is not a new solution or a reach test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from core_to_tail_bvp import Problem


def audit(path: Path, radial: int, angular: int) -> dict:
    raw = path.read_bytes()
    old = json.loads(raw)
    d, n = old["definition"], old["discretization"]
    args = SimpleNamespace(
        radial_free=n["radial_free"], modes=n["modes"],
        design_metric=d["design_metric"], inlet_angles=n["inlet_angles"],
        inlet_state=None, inlet_s=d["inlet_s"], amp2=d["amp2"],
        amp3=d["amp3"], curvature=d["curvature"], length=d["length"],
        cut_radius=d["tail_cut_radius"], flat_start=d["tail_flat_start"],
        cuff_radius=d["tail_cuff_radius"], quadrature=n["tail_quadrature"],
        background=d["background"], beta_wiggle=d.get("beta_wiggle", 0.0),
        fold_min=d.get("fold_min", -0.2),
        fold_first_fraction=d.get("fold_first_fraction", 0.33),
        core_profile=d.get("core_profile", "mixed"),
        ellipse_major=d.get("ellipse_major", 1.0),
        ellipse_minor=d.get("ellipse_minor", 0.3),
        inward_overshoot=d.get("inward_overshoot", 0.2),
        inward_first_fraction=d.get("inward_first_fraction", 0.7),
    )
    p = Problem(args)
    z = np.asarray(old["coefficients"])
    u = np.linspace(0.0, 1.0, radial)
    grid = p.prepare(u, angular)
    g = p.geometry(z, grid, second=True)
    aa = g["a"][:, None]
    ee = np.sum(g["xs"] ** 2, axis=-1) - 1.0
    ff = np.sum(g["xs"] * g["xt"], axis=-1) / aa
    gg = np.sum(g["xt"] ** 2, axis=-1) / aa**2 - 1.0
    rr = np.stack((ee, np.sqrt(2.0) * ff, gg), axis=-1)
    tensor = np.stack((ee, ff, ff, gg), axis=-1).reshape(radial, angular, 2, 2)
    op = np.max(np.abs(np.linalg.eigvalsh(tensor)), axis=-1)
    comp = {}
    for j, name in enumerate(("E_minus_1", "sqrt2_F_over_a", "G_over_a2_minus_1")):
        loc = np.unravel_index(np.argmax(np.abs(rr[:, :, j])), (radial, angular))
        comp[name] = {
            "max_abs": float(abs(rr[loc[0], loc[1], j])),
            "u": float(u[loc[0]]),
            "theta": float(grid["theta"][loc[1]]),
            "rms": float(np.sqrt(np.mean(rr[:, :, j] ** 2))),
        }
    modes = np.fft.rfft(rr, axis=1) / angular
    energy = np.mean(np.sum(np.abs(modes) ** 2, axis=-1), axis=0)
    energy[1:-1] *= 2
    total = float(np.sum(energy))
    spectral = [
        {"mode": int(j), "energy_fraction": float(energy[j] / total)}
        for j in np.argsort(energy)[-8:][::-1]
    ]
    envelope = np.max(op, axis=1)
    peaks = []
    for j in np.argsort(envelope)[::-1]:
        if all(abs(u[j] - item["u"]) > 0.06 for item in peaks):
            peaks.append({"u": float(u[j]), "metric_operator": float(envelope[j])})
        if len(peaks) == 5:
            break
    bounds = np.linspace(0.0, 1.0, 6)
    radial_bins = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        mask = (u >= lo) & (u <= hi)
        radial_bins.append({"u_range": [float(lo), float(hi)],
                            "metric_operator_max": float(np.max(op[mask])),
                            "rms": float(np.sqrt(np.mean(rr[mask] ** 2)))})
    ref = None
    if p.reference is not None:
        beta = p.reference.beta(u)
        ref = {"beta_min": float(np.min(beta)), "beta_max": float(np.max(beta)),
               "radial_free_spline_knots": (np.arange(1, args.radial_free + 1)
                                             / (args.radial_free + 1)).tolist()}
        if hasattr(p.reference, "u1"):
            ref.update(first_beta_join=float(p.reference.u1),
                       exact_flat_start=float(p.reference.u2))
    return {
        "source": str(path), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "background": args.background, "length": args.length,
        "grid": {"radial": radial, "angular": angular},
        "inlet_metric_error": p.inlet_report["sample_relative_metric_op"],
        "metric_operator_max": float(np.max(op)), "components": comp,
        "dominant_angular_residual_modes": spectral,
        "separated_radial_peaks": peaks, "radial_bins": radial_bins,
        "reference": ref,
        "no_optimization_performed": True,
        "new_exact_connector": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="+", type=Path)
    parser.add_argument("--radial", type=int, default=161)
    parser.add_argument("--angular", type=int, default=128)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    payload = {"status": "saved_candidate_development_audit",
               "results": [audit(p, args.radial, args.angular) for p in args.sources],
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.out.write_text(json.dumps(payload, indent=2) + "\n")
    for entry in payload["results"]:
        print(json.dumps({"source": entry["source"],
                          "metric_max": entry["metric_operator_max"],
                          "dominant_modes": entry["dominant_angular_residual_modes"][:4],
                          "radial_peaks": entry["separated_radial_peaks"][:3]}))


if __name__ == "__main__":
    main()
