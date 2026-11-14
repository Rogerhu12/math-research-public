#!/usr/bin/env python3
"""Read-only projected-core and normalized-G transport diagnostics.

The current saved curve is unchanged. No BVP, nonlinear flow integration,
optimization, new tail request, or new candidate is produced. The two inlet
axis values use Fraction on the stored binary coefficients. Optional Gaussian
quadrature of the exact transport identity is a floating diagnostic.
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


def fraction_record(value):
    return {"exact": str(value), "float": float(value)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--linear-port", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--previous-diagnostic", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--orders", type=int, nargs="*", default=[4, 8])
    args = parser.parse_args()
    require(not args.out.exists(), "Refuse an existing report")
    started = time.monotonic()
    cp_id, port_id, diag_id = map(identity, (args.checkpoint, args.linear_port, args.previous_diagnostic))
    require(cp_id["sha256"] == CP_SHA, "Wrong current root checkpoint")
    require(port_id["sha256"] == PORT_SHA, "Wrong frozen port")
    require(diag_id["sha256"] == DIAG_SHA, "Wrong previous fixed-state diagnostic")
    previous = json.loads(args.previous_diagnostic.read_text())
    source_bindings = {row["path"]: row for row in previous["sources"]}
    loader_path = HERE / "db6f-prefix-flat-geometry-source.py"
    require(identity(loader_path) == source_bindings[str(loader_path)], "Original loader identity differs")
    small = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    inputs = [cp_id, port_id, diag_id]
    for chunk in small["pp_coefficient_chunks"]:
        row = identity(args.checkpoint.parent / chunk["file"])
        require(row["bytes"] == chunk["bytes"] and row["sha256"] == chunk["sha256"], "Changed PP chunk")
        inputs.append(row)
    loader = load("core_g_original_flat_loader", loader_path)
    rec, obj, unused_flow, sol = loader.source(args.checkpoint, args.linear_port, args.source_root)
    require(obj.M == 14 and obj.fixed and obj.base_mode == 3, "Wrong fixed core representation")
    require(rec["config"]["angular"] == 512, "Wrong original angular quadrature")
    require(rec["chart"]["values"][0] == 1.0 and rec["chart"]["knots"][0] == 0.0,
            "Initial chart coefficient must be read exactly")
    initial = obj.initial(sol.p).copy()
    flow = obj.Flow(obj.cfg, obj.port, obj.M, obj.q, 512, obj.base_mode, obj.bridge)
    mesh = np.asarray(rec["mesh"], float)
    require(mesh[0] == 0.0 and len(mesh) > 1518, "Unexpected original physical mesh")
    witness = float(mesh[1518])
    endpoints = np.array([0.0, witness])
    endpoint_y = sol.sol(endpoints)
    require(np.array_equal(endpoint_y[:, 0], sol.sol.c[-1, 0, :]), "Inlet is not stored constant PP coefficient")
    q_fraction = F.from_float(float(obj.q))
    e_fraction = 8 * F.from_float(float(rec["warp_reference_q"])) * F.from_float(float(rec["chart"]["values"][0]))
    modes = np.arange(1, obj.M+1)
    axis_rows = []
    axis_weights = []
    for sign, name in ((1, "psi_zero"), (-1, "psi_pi_over_3")):
        weights = np.zeros(obj.n, dtype=np.longdouble)
        weights[0] = 1
        weights[1:obj.M+1] = sign ** modes
        weights[obj.M+1:2*obj.M+1] = (3*modes) * (sign ** modes)
        axis_weights.append(weights)
        rho = 1 - sign*e_fraction
        require(rho > 0, "Noninvertible inlet axis chart")

        def exact_axis(y):
            b = F.from_float(float(y[0]))
            for j in range(1, obj.M+1):
                b += sign**j * (F.from_float(float(y[j])) + 3*j*F.from_float(float(y[obj.M+j])))
            relative_tangent = q_fraction*b/rho
            metric = relative_tangent*(2+relative_tangent)
            return {"B": fraction_record(b), "relative_tangent": fraction_record(relative_tangent),
                    "G_over_a2_minus_1": fraction_record(metric),
                    "abs_G_strictly_exceeds_original_2e_minus_9": abs(metric) > F(1, 500000000)}

        axis_rows.append({"axis": name, "cos_three_psi": sign, "rho_at_core": fraction_record(rho),
                          "saved_core": exact_axis(endpoint_y[:, 0]),
                          "recomputed_initial_callback": exact_axis(initial)})
    weights = np.stack(axis_weights)

    def geometry_scalars(s, y):
        a, ap, _ = flow.profile(np.asarray(s))
        geo = flow.geo(np.asarray(s), 1)
        e = geo["e"]
        ep = -geo["vp"][:, 0] * (1-e)
        signs = np.array([1, -1])[:, None]
        rho = 1-signs*e[None, :]
        rho_s = -signs*ep[None, :]
        b = weights @ np.asarray(y, dtype=np.longdouble)
        relative = np.longdouble(obj.q)*b/(a[None, :]*rho)
        value = relative*(2+relative)
        prefactor = 2*(1+relative)*np.longdouble(obj.q)/(a[None, :]*rho)
        drift = ap[None, :]/a[None, :] + rho_s/rho
        return value, prefactor, drift, b

    endpoint_values, _, _, _ = geometry_scalars(endpoints, endpoint_y)
    for axis_index, row in enumerate(axis_rows):
        row["witness_G_over_a2_minus_1_float"] = float(endpoint_values[axis_index, 1])
        row["endpoint_change_float"] = float(endpoint_values[axis_index, 1]-endpoint_values[axis_index, 0])
    cp_diag = next(row for row in previous["checkpoints"] if row["checkpoint"]["sha256"] == CP_SHA)
    diagnostic = next(row for row in cp_diag["diagnostics"]
                      if row["projection_modes"] == 14 and row["source_quadrature"] == 512)
    old_rows = diagnostic["saved_interpolant"]["rows"]
    first = next(row for row in old_rows if row["s"] == 0.0)
    witness_row = next(row for row in old_rows if abs(row["s"]-witness) < 1e-14)
    previous_scalars = {
        "core_G_FFT_l1": first["G_over_a2_error_FFT_l1"],
        "witness_G_FFT_l1": witness_row["G_over_a2_error_FFT_l1"],
        "ten_point_G_max": diagnostic["saved_interpolant"]["max_G_FFT_l1"],
    }

    # Snapshot only.  All endpoints and every polynomial/chart knot are kept;
    # no material node or coefficient is changed to perform this quadrature.
    candidates = np.r_[mesh, flow.breaks, np.asarray(rec["chart"]["knots"])*flow.end,
                       .75*flow.end, 0.0, witness]
    knots = np.unique(candidates[(candidates >= 0.0) & (candidates <= witness)])
    require(knots[0] == 0.0 and knots[-1] == witness, "Wrong integration interval")
    transport = []
    for order in args.orders:
        require(order >= 2 and order <= 16, "Diagnostic quadrature order outside declared range")
        abscissa, gauss_weights = np.polynomial.legendre.leggauss(order)
        lengths = np.diff(knots)
        sample_s = (knots[:-1, None] + lengths[:, None]*(abscissa[None, :]+1)/2).ravel()
        sample_w = (lengths[:, None]*gauss_weights[None, :]/2).ravel().astype(np.longdouble)
        totals = np.zeros((3, 2), dtype=np.longdouble)
        pointwise_max = np.zeros((3, 2), dtype=np.longdouble)
        for start in range(0, len(sample_s), 64):
            ss = sample_s[start:start+64]
            ww = sample_w[start:start+64]
            yy = sol.sol(ss)
            yp = sol.sol(ss, 1)
            rhs = flow.fun(ss, yy, sol.p)
            _, pref, drift, b = geometry_scalars(ss, yy)
            byp = weights @ np.asarray(yp, dtype=np.longdouble)
            brhs = weights @ np.asarray(rhs, dtype=np.longdouble)
            total_derivative = pref*(byp-b*drift)
            galerkin_derivative = pref*(brhs-b*drift)
            interpolant_derivative = pref*(weights @ np.asarray(yp-rhs, dtype=np.longdouble))
            for index, values in enumerate((total_derivative, galerkin_derivative, interpolant_derivative)):
                totals[index] += np.sum(values*ww[None, :], axis=1)
                pointwise_max[index] = np.maximum(pointwise_max[index], np.max(np.abs(values), axis=1))
        components = []
        for axis_index, row in enumerate(axis_rows):
            change = endpoint_values[axis_index, 1]-endpoint_values[axis_index, 0]
            components.append({"axis": row["axis"],
                "endpoint_change": float(change),
                "integrated_total_derivative": float(totals[0, axis_index]),
                "integrated_projected_source_contribution": float(totals[1, axis_index]),
                "integrated_saved_interpolant_minus_RHS_contribution": float(totals[2, axis_index]),
                "quadrature_endpoint_closure_error": float(totals[0, axis_index]-change),
                "quadrature_split_closure_error": float(totals[0, axis_index]-totals[1, axis_index]-totals[2, axis_index]),
                "maximum_sampled_total_derivative": float(pointwise_max[0, axis_index]),
                "maximum_sampled_projected_source_contribution": float(pointwise_max[1, axis_index]),
                "maximum_sampled_interpolant_contribution": float(pointwise_max[2, axis_index])})
        transport.append({"quadrature_order": order, "pieces": len(knots)-1,
                          "quadrature_points": len(sample_s), "components": components})

    sources = [identity(__file__)]
    for module in list(sys.modules.values()):
        file = getattr(module, "__file__", None)
        if not file:
            continue
        path = Path(file).resolve()
        if path.suffix == ".py" and path.is_relative_to(TOPIC) and path != Path(__file__).resolve():
            current = identity(path)
            require(str(path) in source_bindings and current == source_bindings[str(path)],
                    "Original imported source not equal to the previous bound diagnostic: "+str(path))
            sources.append(current)
    sources = list({row["path"]:row for row in sources}.values())
    for row in inputs+sources:
        require(identity(row["path"]) == row, "Input/source changed during diagnosis")
    report = {
        "scope": __doc__, "schema": "78718-core-normalized-G-transport-v1",
        "status": "COMPLETED_READ_ONLY_CURRENT_CURVE_DIAGNOSTIC",
        "checkpoint": cp_id, "input_bindings": inputs, "source_bindings": sources,
        "original_native_witness_node": 1518, "witness_s": witness,
        "parameters_unchanged": True, "all_14_support_coefficients_used": True,
        "inlet_physical_coefficient_difference_from_callback": float(obj.q*np.max(np.abs(endpoint_y[:, 0]-initial))),
        "axis_values": axis_rows, "previous_bound_report_scalars": previous_scalars,
        "transport": transport,
        "transport_identity": "D_s(G/a^2-1)=2/a^2 * F_u dot D_u(actual_material_velocity-raw_Frenet_velocity)",
        "chart_axis_identity": "sin(3*psi)=0; both axes have u=psi at every s, but rho_s is retained",
        "BVP_calls": 0, "tail_calls": 0, "nonlinear_flow_integrations": 0,
        "new_candidate": False, "continuous_transport_bound": False,
        "seconds": time.monotonic()-started,
    }
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    require(args.out.stat().st_size < 5_000_000, "Per-file limit")
    print(json.dumps({"status": report["status"], "output": identity(args.out),
        "core_axis_G": {row["axis"]:row["saved_core"]["G_over_a2_minus_1"]["float"] for row in axis_rows},
        "core_axis_exceeds_original_tol": {row["axis"]:row["saved_core"]["abs_G_strictly_exceeds_original_2e_minus_9"] for row in axis_rows},
        "previous_report_scalars": previous_scalars, "transport_orders": args.orders,
        "BVP_calls": 0, "tail_calls": 0, "seconds": report["seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
