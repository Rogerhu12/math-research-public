#!/usr/bin/env python3
"""Independent Bessel check of the fixed angular-chart linear DN matrix.

Finite numerical verification only. The identities compared here are derived
in the audit note. No tail solve or prefix optimization is performed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.special import jv


def run(port_file: Path, mode_count: int, e: float, nodes: int) -> dict:
    port = json.loads(port_file.read_text())
    d = np.asarray(port["linearSlope"], float)
    k = np.arange(1, len(d) + 1, dtype=float)[:, None]
    j = np.arange(1, mode_count + 1, dtype=float)[None, :]
    to_bessel = (j / k) * (jv(k - j, k * e) - jv(k + j, k * e))
    from_bessel = (jv(k - j, k * e) + jv(k + j, k * e)).T
    output_means = jv(k[:, 0], k[:, 0] * e)
    mean_row_bessel = (output_means * d) @ to_bessel
    dn_bessel = (from_bessel * d[None, :]) @ to_bessel

    psi = 2 * np.pi * np.arange(nodes) / nodes
    theta = psi - e * np.sin(3 * psi) / 3
    rho = 1 - e * np.cos(3 * psi)
    physical = np.cos(3 * k * theta)
    chart = np.cos(3 * j.T * psi)
    to_quadrature = 2 / nodes * np.einsum("kp,jp,p->kj", physical, chart, rho)
    from_quadrature = 2 / nodes * chart @ physical.T
    dn_quadrature = (from_quadrature * d[None, :]) @ to_quadrature
    mean_row_quadrature = (physical.mean(axis=1) * d) @ to_quadrature
    input_physical_mean = np.mean(chart * rho, axis=1)
    exact_input_physical_mean = np.zeros(mode_count)
    exact_input_physical_mean[0] = -e / 2

    return {
        "scope": "Independent finite coefficient identity check only; floating arithmetic has no interval enclosure.",
        "port_file": str(port_file), "port_sha256": hashlib.sha256(port_file.read_bytes()).hexdigest(),
        "parameters": {"psi_modes": mode_count, "physical_modes": len(d), "e": e, "nodes": nodes},
        "max_to_matrix_difference": float(abs(to_bessel - to_quadrature).max()),
        "max_from_matrix_difference": float(abs(from_bessel - from_quadrature).max()),
        "max_dn_matrix_difference": float(abs(dn_bessel - dn_quadrature).max()),
        "max_output_mean_row_difference": float(abs(mean_row_bessel - mean_row_quadrature).max()),
        "max_input_physical_mean_difference": float(abs(input_physical_mean - exact_input_physical_mean).max()),
        "linear_output_psi_mean_row": mean_row_bessel.tolist(),
        "physical_input_mean": exact_input_physical_mean.tolist(),
        "linear_mean_is_not_zero": bool(np.max(abs(mean_row_bessel)) > 1e-10),
        "dn_max_abs_entry": float(abs(dn_bessel).max()),
        "unpaid": ["infinite physical-frequency DN cutoff", "nonlinear mean response", "Cartesian two-jet seam"]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=Path, required=True)
    parser.add_argument("--modes", type=int, default=8)
    parser.add_argument("--e", type=float, default=0.64)
    parser.add_argument("--nodes", type=int, default=8192)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Refusing to overwrite an audit record")
    result = run(args.port, args.modes, args.e, args.nodes)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("max_dn_matrix_difference", "max_output_mean_row_difference", "linear_output_psi_mean_row")}))
