#!/usr/bin/env python3
"""Static re-projection of one fixed current exact support core.

The same 14 physical support coefficients and fixed angular chart are used at
every projection order. This is not zero padding of the saved curve, a solved
higher-mode curve, a BVP, or a new candidate. No tail is requested.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from types import SimpleNamespace
import time

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import numpy as np

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
CP_SHA = "4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a"
PORT_SHA = "500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702"
DIAG_SHA = "53641e7e8ceb2ea822794a9df5404807a5162aa704aa9ee35be99b3c2d86dbfe"


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exact_axes(y, q, warp_reference):
    modes = (len(y)-1)//3
    result = {}
    for sign, name in ((1, "psi_zero"), (-1, "psi_pi_over_3")):
        b = F.from_float(float(y[0]))
        for j in range(1, modes+1):
            b += sign**j * (F.from_float(float(y[j])) + 3*j*F.from_float(float(y[modes+j])))
        rho = 1-sign*8*F.from_float(float(warp_reference))
        r = F.from_float(float(q))*b/rho
        value = r*(2+r)
        result[name] = {"G_over_a2_minus_1": float(value), "exact": str(value),
                        "abs_strictly_above_2e_minus_9": abs(value) > F(1, 500000000)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--linear-port", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--bound-diagnostic", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), "Refuse existing output")
    started = time.monotonic()
    cp_id, port_id, diag_id = map(identity, (args.checkpoint, args.linear_port, args.bound_diagnostic))
    require(cp_id["sha256"] == CP_SHA and port_id["sha256"] == PORT_SHA and diag_id["sha256"] == DIAG_SHA,
            "Wrong declared source input")
    old_diagnostic = json.loads(args.bound_diagnostic.read_text())
    bound_sources = {row["path"]:row for row in old_diagnostic["sources"]}
    inputs = [cp_id, port_id, diag_id]
    small = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    for chunk in small["pp_coefficient_chunks"]:
        row = identity(args.checkpoint.parent/chunk["file"])
        require(row["bytes"] == chunk["bytes"] and row["sha256"] == chunk["sha256"], "Changed saved PP chunk")
        inputs.append(row)
    loader_path = HERE/"db6f-prefix-flat-geometry-source.py"
    require(identity(loader_path) == bound_sources[str(loader_path)], "Changed original source loader")
    loader = load("fixed_core_reprojection_loader", loader_path)
    rec, obj, flow, sol = loader.source(args.checkpoint, args.linear_port, args.source_root)
    require(obj.fixed and obj.M == 14 and obj.base_mode == 3, "Wrong fixed source class")
    require(rec["chart"]["values"][0] == 1.0, "Initial chart value changed")
    # Replay the literal original saved parameters, rather than rescaling them
    # when the representation order changes. No extra support coefficients are
    # introduced. Keep the gauge amplitude distinct from the support amplitude.
    saved_p = np.asarray(rec["parameters"], float)
    require(np.array_equal(obj.pscale, np.asarray(rec["central_correction_scales"], float)),
            "Saved support normalization scales differ")
    callback = obj.initial(saved_p).copy()
    core = obj._core
    fixed_coefficients = core.coefficients.copy()
    require(len(fixed_coefficients) == 14, "Wrong actual support coefficient count")
    require(obj.support_amplitude == rec["actual_primary_amplitude"], "Literal saved amplitude replay differs")
    coefficient_sha = hashlib.sha256(np.asarray(fixed_coefficients, dtype="<f8").tobytes()).hexdigest()
    from curve_stable_prefix_bvp import CylindricalPrefix
    orders = [14, 15, 16, 18, 22, 26]
    quadratures = [2048, 4096]
    rows = []
    original_callback_match = None
    core_metric_max = 0.0
    for n in quadratures:
        angular = flow.angular(n)
        exact = core.evaluate(angular[1])
        core_metric_max = max(core_metric_max, float(np.max(np.abs(np.sum(exact["Ft"]**2, axis=1)-1))))
        perturbation = exact["F"]-angular[4]
        exact_first = exact["Ft"]*angular[2][:, None]
        exact_second = exact["Ftt"]*angular[2][:, None]**2+exact["Ft"]*angular[3][:, None]
        for modes in orders:
            carrier = SimpleNamespace(M=modes, n=3*modes+1, even=3*np.arange(1, modes+1))
            b, b1, b2 = CylindricalPrefix.basis(carrier, n)
            # Match initial()'s divide-by-gauge and later multiplication exactly.
            normalized = CylindricalPrefix.project(perturbation[None, :, :], b)[:, 0]/obj.q
            physical = obj.q*normalized
            reconstructed = angular[4]+CylindricalPrefix.values(physical[:, None], b)[0]
            first = angular[5]+CylindricalPrefix.values(physical[:, None], b1)[0]
            second = angular[6]+CylindricalPrefix.values(physical[:, None], b2)[0]
            metric = np.sum(first*first, axis=1)/angular[2]**2-1
            record = {"projection_modes": modes, "source_quadrature": n,
                      "support_coefficient_count_unchanged": len(fixed_coefficients),
                      "support_coefficients_sha256_little_endian_f64": coefficient_sha,
                      "G_relative_FFT_l1": float(np.sum(np.abs(np.fft.fft(metric)/n))),
                      "G_relative_max_sampled": float(np.max(np.abs(metric))),
                      "position_error_max_sampled": float(np.max(np.linalg.norm(reconstructed-exact["F"], axis=1))),
                      "first_jet_error_max_sampled": float(np.max(np.linalg.norm(first-exact_first, axis=1))),
                      "second_jet_error_max_sampled": float(np.max(np.linalg.norm(second-exact_second, axis=1))),
                      "axes": exact_axes(normalized, obj.q, rec["warp_reference_q"])}
            rows.append(record)
            if modes == 14 and n == 2048:
                original_callback_match = float(obj.q*np.max(np.abs(normalized-callback)))
            require(np.array_equal(core.coefficients, fixed_coefficients), "Support core mutated")
    require(original_callback_match == 0.0, "Direct M14/N2048 projection differs from original initial callback")
    sources = [identity(__file__)]
    for module in list(sys.modules.values()):
        name = getattr(module, "__file__", None)
        if not name:
            continue
        path = Path(name).resolve()
        if path.suffix == ".py" and path.is_relative_to(TOPIC) and path != Path(__file__).resolve():
            row = identity(path)
            require(str(path) in bound_sources and row == bound_sources[str(path)], "Original source changed: "+str(path))
            sources.append(row)
    sources = list({row["path"]:row for row in sources}.values())
    for row in inputs+sources:
        require(identity(row["path"]) == row, "Input changed during read-only diagnosis")
    report = {"schema": "78718-fixed-support-core-reprojection-v1", "scope": __doc__,
              "status": "COMPLETED_STATIC_REPROJECTION_OF_ONE_FIXED_CORE",
              "input_bindings": inputs, "source_bindings": sources,
              "gauge_amplitude": obj.q, "actual_support_amplitude": obj.support_amplitude,
              "literal_saved_parameters_replayed": True, "original_scaling_factors_verified": True,
              "fixed_support_coefficient_count": 14, "fixed_support_coefficients_sha256_little_endian_f64": coefficient_sha,
              "M14_N2048_callback_physical_coefficient_max_difference": original_callback_match,
              "exact_core_unit_tangent_max_floating_error": core_metric_max,
              "rows": rows, "new_candidate": False, "saved_curve_zero_padding": False,
              "BVP_calls": 0, "tail_calls": 0, "flow_integrations": 0,
              "continuous_FFT_bound": False, "seconds": time.monotonic()-started}
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    require(args.out.stat().st_size < 5_000_000, "Per-file limit")
    selected = {str(row["projection_modes"]):row["G_relative_FFT_l1"] for row in rows if row["source_quadrature"] == 4096}
    print(json.dumps({"status": report["status"], "output": identity(args.out),
                     "M14_callback_max_difference": original_callback_match,
                     "fixed_core_projection_G_FFT_l1_at_N4096": selected,
                     "BVP_calls": 0, "tail_calls": 0, "seconds": report["seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
